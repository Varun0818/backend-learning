DEFAULT_JOB = {"status": "pending", "attempts": 0}


def build_job(payload):
    job = DEFAULT_JOB.copy()
    job["id"] = payload["id"]
    job["url"] = payload["url"]
    return job


def record_attempt(job, ok):
    job["attempts"] = job["attempts"] + 1
    if ok:
        job["status"] = "done"
    else:
        job["status"] = "failed"
    return job


def run(payloads, results):
    jobs = []
    for p in payloads:
        jobs.append(build_job(p))
        print(jobs)
    for job, ok in zip(jobs, results):
        record_attempt(job, ok)
    return jobs


if __name__ == "__main__":
    payloads = [
        {"id": "a1", "url": "https://example.com/a"},
        {"id": "b2", "url": "https://example.com/b"},
        {"id": "c3", "url": "https://example.com/c"},
    ]
    for job in run(payloads, [True, False, True]):
        print(job["id"], job["url"], job["status"], job["attempts"])
