import os

import gradio as gr


GOLDEN_INPUT = (
    "Every Monday I open Jira to check my weekly to-dos. "
    "I pick the high-priority ones, pull the numbers from our dashboard, "
    "write a short report for each, and send it to my manager on Slack."
)

GOLDEN_OUTPUT = """Repeatable steps I found:
1. Open Jira and list this week's to-dos (every Monday)
2. Pick the high-priority tasks (every Monday)
3. Pull numbers from the dashboard (per task)
4. Write a short report (per task)
5. Send the report to your manager on Slack (per task)

What to do with each step:
1. Automate: a saved Jira filter lists them for you
2. Keep human: you decide what matters this week
3. Automate: export the same dashboard view each time
4. Automate a first draft, keep human for the final edit
5. Keep human until the draft is trusted

This week: save one Jira filter for your high-priority to-dos."""


def respond(message, history):
    if "jira" in message.lower():
        return GOLDEN_OUTPUT
    return ("Tell me your weekly workflow step by step: "
            "what you open first, what you do next, and who gets the result.")


demo = gr.ChatInterface(
    fn=respond,
    examples=[GOLDEN_INPUT],
    title="Aarav's Workflow Planner v2",
)
# Laptop: opens on port 7860. Render: uses the port Render hands the app.
demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
