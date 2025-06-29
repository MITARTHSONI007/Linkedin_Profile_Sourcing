from agent import LinkedInSourcingAgent
from config import settings
import sys
import asyncio

def print_candidates(scored):
    for idx, c in enumerate(scored, 1):
        print(f"{idx}. {c['name']} | {c['linkedin_url']} | Score: {c['fit_score']} | Breakdown: {c['score_breakdown']}")

def print_messages(messages):
    for m in messages:
        print(f"\nTo: {m['candidate']} ({m['linkedin_url']})\nMessage: {m['message']}\n")

async def main():
    agent = LinkedInSourcingAgent()
    # For demo: use a hardcoded job description or accept input
    if len(sys.argv) > 1:
        job_description = ' '.join(sys.argv[1:])
    else:
        job_description = (
            "Software Engineer, ML Research at Windsurf. "
            "Looking for someone to train LLMs for code generation, $140-300k + equity, Mountain View. "
            "Skills: Python, Machine Learning, Deep Learning, Backend, API, LLM. "
            "Elite schools preferred."
        )
    print("\n[1] Searching for LinkedIn candidates...")
    candidates = await agent.search_linkedin(job_description, max_results=10)
    print(f"Found {len(candidates)} candidates.")
    print("\n[2] Scoring candidates...")
    scored = agent.score_candidates(candidates, job_description)
    print_candidates(scored)
    print("\n[3] Generating outreach messages for top 5...")
    messages = agent.generate_outreach(scored[:5], job_description)
    print_messages(messages)

if __name__ == "__main__":
    asyncio.run(main())
