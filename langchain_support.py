from langchain.tools import Tool

# A simple rule-based career recommendation function
def career_recommendation(query: str) -> str:
    # Example mapping (replace with real logic or Google Sheets backend)
    if "AI" in query or "data" in query.lower():
        return "You’d be a great fit for a Data Scientist or ML Engineer role."
    elif "design" in query.lower():
        return "Consider UI/UX Designer or Creative Director."
    elif "business" in query.lower():
        return "Product Manager or Business Analyst could be good."
    else:
        return "I’d recommend exploring Software Engineering as a versatile option."

career_tool = Tool(
    name="CareerAdvisor",
    func=career_recommendation,
    description="Suggests career paths based on user interests and skills."
)
