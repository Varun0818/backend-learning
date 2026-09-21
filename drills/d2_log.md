# D2 — Git Remote / Merge Conflict

## Tried
- Pushed `clone1` successfully to the remote.
- Tried pushing `clone2` and got a `fetch first` rejection because the remote had `a1f6138`, which clone2 did not contain.
- Ran `git pull` in clone2. Git first stopped because the branches had diverged and a pull strategy had not been configured.
- Configured pull to use merge and pulled again.
- Git produced a merge conflict in `record/position.md` because clone1 and clone2 had changed the same `updated:` line.
- Resolved the conflict manually by removing the conflict markers and keeping a normal permanent `updated:` line.
- Committed the resolution as `ac95f46` with the message `resolve remote merge conflict`.
- Pushed clone2 successfully.
- Pulled in clone1 and verified that both clones had the same top five commits.

## Expected
- Expected clone1's push to succeed.
- Expected clone2's push to be rejected because the remote had changes it did not have locally.
- Expected the merge to produce a conflict because both clones changed the same line in `record/position.md`.
- Expected the final push after resolving the conflict to succeed.
- Expected both clones to eventually contain the same history.

## Actual
- Clone1 pushed successfully: `fb96b2f..a1f6138`.
- Clone2 push was rejected with `fetch first`.
- The first `git pull` stopped because Git required a strategy for reconciling divergent branches.
- After choosing merge, the pull produced a conflict in `record/position.md`.
- The conflict was resolved manually.
- The resolution was committed as `ac95f46`.
- Clone2 pushed successfully: `a1f6138..ac95f46`.
- Clone1 then fast-forwarded to `ac95f46`.
- Both clones showed the same five commits at the top:
  - `ac95f46 resolve remote merge conflict`
  - `4cce458 edit position from clone2`
  - `a1f6138 edit position from clone1`
  - `fb96b2f record session 4 position: debugging persistence measured`
  - `a779b0a fix shared job state caused by dictionary aliasing`
