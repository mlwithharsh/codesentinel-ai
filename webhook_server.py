from fastapi import FastAPI, Request
from agents.orchestrator import CodeSentinelOrchestrator
from agents.report_formatter import PRCommentFormatter

app = FastAPI()

orchestrator = CodeSentinelOrchestrator()
formatter = PRCommentFormatter()

@app.post("/github-webhook")
async def github_webhook(request: Request):

    payload = await request.json()

    # Simulate extracting code from PR diff
    # For now assume payload contains "code"
    code_snippet = payload.get("code")

    if not code_snippet:
        return {"error": "No code provided"}

    report = orchestrator.analyze_code(code_snippet)
    comment = formatter.format_comment(report)

    return {
        "status": "analysis_complete",
        "comment": comment
    }