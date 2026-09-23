
# gate0 Acceptance Criteria

## 1. all runs without none or missing error

**Input:**

[{"id": 1, "error": 0}, {"id": 2, "error": ""},{"id" : 3, "error": False}]

**Expected output:**

[1,2,3]

Every run in the input must appear in the output.

## 2. input with missing Error with Error : None

**Input:**

[{"id": 1, "error": None}, {"id":4,"error":""}, {"id":3}, {"id": 2, "error": 3}, {"id": 5, "error": 3}, {"id":6}]

**Expected output:**

[4,2,5]

Only run_ids whose error key is present and not None

## 3. Every run has either None as Error or missing the Error key

**Input:**

[{"id": 1, "error": None}, {"id": 2, "error": None}, {"id" : 3}]

**Expected output:**

[]

An empty list should be the result

## 4. Empty input

**Input:**

[]

**Expected output:**

[]

An empty input list returns an empty list.

## 5. Input must not be modified

**Input before the function call:**

[{"id": 2, "error": ""}, {"id": 1, "error": False}, {"id": 3, "error" : 0}, {"id": 5, "error" : ""}, {"id": 4, "error" : 10}]

**Expected return:**

[2,1,3,5,4]

**Input after the function call:**

[{"id": 2, "error": ""}, {"id": 1, "error": False}, {"id": 3, "error" : 0}, {"id": 5, "error" : ""}, {"id": 4, "error" : 10}]

The original input list and its order data must remain unchanged after the function call.

[2,1,3,5,4]
