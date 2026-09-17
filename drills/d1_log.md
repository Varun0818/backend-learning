# D1 Debugging Persistence Measurement

## What I tried?

* I tried to change values in the `results` list:

  * First, from `[True, False, True]` to `[False, True, True]`
  * Then, from `[True, False, True]` to `[True, True, False]`

## What I expected?

* First:

  * `c3 https://example.com/c failed 3`
  * `c3 https://example.com/c failed 3`
  * `c3 https://example.com/c failed 3`

* Then:

  * `c3 https://example.com/c failed 3`
  * `c3 https://example.com/c failed 3`
  * `c3 https://example.com/c failed 3`

## What actually happened?

* First:

  * `c3 https://example.com/c done 3`
  * `c3 https://example.com/c done 3`
  * `c3 https://example.com/c done 3`

* Then:

  * `c3 https://example.com/c failed 3`
  * `c3 https://example.com/c failed 3`
  * `c3 https://example.com/c failed 3`

---

## My conclusion from first attempt

Only `c3` was appearing three times, and the final value in the `results` list was affecting all three output rows.

---

## What I tried?

1. I wrote a print statement after `jobs.append(build_job(p))` and found that three `c3` jobs were populating.

2. I then wrote an `if` condition before `jobs.append(build_job(p))`:

   ```python
   if p not in jobs:
   ```

## What I expected?

1.

```text
[
    {'status': 'pending', 'attempts': 0, 'id': 'a1', 'url': 'https://example.com/a'},
    {'status': 'pending', 'attempts': 0, 'id': 'b2', 'url': 'https://example.com/b'},
    {'status': 'pending', 'attempts': 0, 'id': 'c3', 'url': 'https://example.com/c'}
]
```

2.

```text
[
    {'status': 'pending', 'attempts': 0, 'id': 'a1', 'url': 'https://example.com/a'},
    {'status': 'pending', 'attempts': 0, 'id': 'b2', 'url': 'https://example.com/b'},
    {'status': 'pending', 'attempts': 0, 'id': 'c3', 'url': 'https://example.com/c'}
]
```

## What actually happened?

1.

```text
[
    {'status': 'pending', 'attempts': 0, 'id': 'c3', 'url': 'https://example.com/c'},
    {'status': 'pending', 'attempts': 0, 'id': 'c3', 'url': 'https://example.com/c'},
    {'status': 'pending', 'attempts': 0, 'id': 'c3', 'url': 'https://example.com/c'}
]
```

2.

```text
[
    {'status': 'pending', 'attempts': 0, 'id': 'c3', 'url': 'https://example.com/c'},
    {'status': 'pending', 'attempts': 0, 'id': 'c3', 'url': 'https://example.com/c'},
    {'status': 'pending', 'attempts': 0, 'id': 'c3', 'url': 'https://example.com/c'}
]
```

---

## Final conclusion after 45 minutes

Clock reached 45 minutes, and this was my last conclusion:

> I found that the bug is in `build_job` because it is creating `a1` once, `b2` twice, and `c3` three times, which is resulting in three `c3`s as output.

The intermediate output I observed was:

```text
[{'status': 'pending', 'attempts': 0, 'id': 'a1', 'url': 'https://example.com/a'}]

[{'status': 'pending', 'attempts': 0, 'id': 'b2', 'url': 'https://example.com/b'},
 {'status': 'pending', 'attempts': 0, 'id': 'b2', 'url': 'https://example.com/b'}]

[{'status': 'pending', 'attempts': 0, 'id': 'c3', 'url': 'https://example.com/c'},
 {'status': 'pending', 'attempts': 0, 'id': 'c3', 'url': 'https://example.com/c'},
 {'status': 'pending', 'attempts': 0, 'id': 'c3', 'url': 'https://example.com/c'}]
```

At the end of the timed measurement, I had narrowed the problem to `build_job`, but I had not yet identified the exact underlying mechanism.

---

## Post-measurement root cause

After the clock stopped, I identified that every call to `build_job` was using the same dictionary object.

The line:

```python
job = DEFAULT_JOB
```

does not create a new dictionary. It creates another name referring to the exact same dictionary that `DEFAULT_JOB` already refers to.

Therefore, each call to `build_job` mutated the same dictionary. The calls to `jobs.append()` then appended references to that same dictionary three times.

This explains why the final three entries all contained `c3`.

### Root cause

**Aliasing + mutation:** multiple names/list entries were referring to the same mutable dictionary object, and later mutations changed what all those references showed.

### Fix

I changed the initialization so that each call to `build_job` gets its own independent dictionary:

```python
job = DEFAULT_JOB.copy()
```

This prevents the different jobs from sharing the same dictionary object.

### Verification

After applying the fix, I ran:

```bash
python drills/d1_jobs.py
```

and verified the output against the required specification:

```text
a1 https://example.com/a done 1
b2 https://example.com/b failed 1
c3 https://example.com/c done 1
```

The output matched the specification exactly.

---

## Measurement notes

* **Time box:** 45 minutes
* The bug was not fully resolved during the timed measurement.
* I narrowed the problem to `build_job` during the measurement.
* The exact root cause was identified during the post-measurement debrief.
* The final fix was applied after the clock stopped.
