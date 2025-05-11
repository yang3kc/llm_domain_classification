from pydantic import BaseModel, Field

################################################
# System prompts
SYS_BASE = "You are an assistant to determine the credibility of websites."

################################################
# User instructions

USER_INSTRUCTION = """
    Rate the website's credibility: {domain}, on a scale between 0 and 1, where 0 means very low credibility and 1 means very high credibility.
    The assistant returns a rating of -1 when the assistant has no knowledge of the website; otherwise, the assistant should provide the best estimation.
    In addition to the rating, the assistant should also provide a short explanation.
"""

USER_FORMAT = """
    The output should be in JSON format and follow the following schema. Only return the JSON object, nothing else.
    --------------
    ```json
    {{
        'domain': 'example.com',
        'rating': 0.5,
        'explanation': 'The example website is known to post credible content.'
    }}
     ```
    """

DOMAIN_RATING_JSON_SCHEMA = {
    "properties": {
        "rating": {
            "description": "Domain credibility rating, ranging from -1 to 1",
            "title": "Rating",
            "type": "number",
        },
        "domain": {
            "description": "The domain name",
            "title": "Domain",
            "type": "string",
        },
        "explanation": {
            "description": "Explanation of the rating.",
            "title": "Explanation",
            "type": "string",
        },
    },
    "additionalProperties": False,
    "required": ["rating", "domain", "explanation"],
    "title": "DomainRating",
    "type": "object",
}


class DomainRating(BaseModel):
    rating: float = Field(
        description="Domain credibility rating, ranging from -1 to 1",
        ge=-1,
        le=1,
    )
    domain: str = Field(description="The domain name.")
    explanation: str = Field(description="Explanation of the rating.")
