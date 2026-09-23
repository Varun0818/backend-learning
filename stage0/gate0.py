def failed_ids(runs):
    result=[]
    for run in runs:
        if run.get("error") or run.get("error")== False or run.get("error")=="":
            result.append(run["id"])
    return result


