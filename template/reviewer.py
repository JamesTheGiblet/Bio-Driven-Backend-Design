def review_architecture(description: str) -> str:
    feedback = []
    if "monolith" in description:
        feedback.append("Consider splitting into organs (microservices).")
    if "auth" in description:
        feedback.append("Auth can be treated like an immune system – isolate and protect.")
    return "\n".join(feedback) if feedback else "Architecture seems biologically sound."