# G5 Inventory

## 1. Workflow exports

### Lead_scoring.json

- JSON file line count: 2174
- Code nodes: 13
- Actual JS logic: 953 lines
- Important distinction: JSON line count includes the complete workflow definition, node configuration, connections, metadata, etc. JS line count refers only to the JavaScript contained inside the Code nodes.

### LSE_Dashboard_API.json.json

- JSON file line count: 946
- Code nodes: 4
- Actual JS logic: 94 lines

---

## 2. Lead_scoring.json — Code-node inventory

1. Get rows from sheet and add run IDs — 8 lines
2. Prepare row JSON formatting, fetch information from all sheets, and create a proper row — 8 lines
3. Compute the priority ranks — 19 lines
4. Extract the domain from the previous OpenAI node — 30 lines
5. Generate search queries — 51 lines
6. Clean and format the data returned by the previous node — 124 lines
7. Clean and format the Tavily search results — 43 lines
8. Reduce the data by row — 34 lines
9. Explode blobs by truncating the content to 4,000 characters and cleaning the content — 63 lines
10. Parse the whole input and return the source events — 89 lines
11. Find duplicate events and deduplicate them — 100 lines
12. Deduplicate the signals — 70 lines
13. Score the signals using different predefined rules — 314 lines

---

## 3. LSE_Dashboard_API.json.json — Code-node inventory

1. **Build Company Rows** — 20 lines
   - Preceded by Webhook: Add Companies (`n8n-nodes-base.webhook`)
   - Followed by Append to Prospects_Input (`n8n-nodes-base.googleSheets`)

2. **Combine Dashboard Data** — 25 lines
   - Preceded by Read Query_Config (`n8n-nodes-base.googleSheets`)
   - Followed by Respond: Dashboard Data (`n8n-nodes-base.respondToWebhook`)

3. **Prepare Review Update** — 23 lines
   - Preceded by Webhook: Review Action (`n8n-nodes-base.webhook`)
   - Followed by Update Review Status (`n8n-nodes-base.googleSheets`)

4. **Prepare Config Update** — 26 lines
   - Preceded by Webhook: Query Config Update (`n8n-nodes-base.webhook`)
   - Followed by Update Query_Config Row (`n8n-nodes-base.googleSheets`)

---

## 4. Stack

### Lead scoring

The workflow takes ICP-satisfied companies as input and then gathers information about each target from their personal/company website, news, search, and other external sources. The collected information is then cleaned, formatted, deduplicated, and converted into signals. These signals are finally scored using predefined rules so that the highest-priority targets can be identified for outreach.

In simple terms:

**ICP-qualified companies → information gathering → search/news signals → cleaning & formatting → deduplication → signal scoring → top-priority targets for outreach**

### Dashboard API

The workflow is itself a small API rather than a client making outbound HTTP requests.

The stack is:

**Webhook-triggered endpoints → JavaScript transformation → Google Sheets data operations → `respondToWebhook` responses**

The important correction was that the HTTP POST/GET labels describe the webhook's HTTP interface; they are not HTTP Request nodes making outbound API calls.

---

## 5. Git status

- The exported JSON files are **not tracked by Git**.
- They were exported from n8n and currently live in the Downloads folder.
- n8n's own versioning is separate from Git version control.

---

## 6. Does it run?

**Yes — verified.**

For the workflow to run, the following were verified:

- n8n instance is available and reachable.
- OpenAI credentials are available and working.
- Tavily credentials are available and working.
- Firecrawl credentials are available and working.
- A populated Google Sheet is available and working.
- The required external services are reachable.

The JSON export itself is only the workflow definition. Execution requires the workflow to exist in the n8n environment together with its configured credentials, input data, and external service access.

---

## 7. Final inventory

- Total Code nodes: 17
- Lead_scoring.json: 13
- LSE_Dashboard_API.json.json: 4
- Git: not tracked
- Runtime: verified as runnable
