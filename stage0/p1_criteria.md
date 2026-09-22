# P1 Acceptance Criteria

## 1. Multiple distinct customers

**Input:**

[{"customer": "varun", "amount": 500}, {"customer": "amit", "amount": 300}]

**Expected output:**

{"varun": 500, "amit": 300}

Every customer appearing in the input must appear in the output.

## 2. Repeated customer

**Input:**

[{"customer": "amit", "amount": 500}, {"customer": "amit", "amount": 300}]

**Expected output:**

{"amit": 800}

Amounts for the same customer must be summed.

## 3. Customer with a zero total

**Input:**

[{"customer": "varun", "amount": 500}, {"customer": "varun", "amount": -500}]

**Expected output:**

{"varun": 0}

A customer whose total is zero must still appear in the output.

## 4. Empty input

**Input:**

[]

**Expected output:**

{}

An empty input list returns an empty dictionary.

## 5. Input must not be modified

**Input before the function call:**

[{"customer": "varun", "amount": 500}, {"customer": "amit", "amount": 300}]

**Expected return:**

{"varun": 500, "amit": 300}

**Input after the function call:**

[{"customer": "varun", "amount": 500}, {"customer": "amit", "amount": 300}]

The original input list and its order data must remain unchanged after the function call.
