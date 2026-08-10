from pydantic import BaseModel, Field
from typing import List, Literal


Category = Literal[
    "Learning",
    "Networking",
    "Career",
    "Technical Skills",
    "Events & Conferences",
    "Other",
]

Sentiment = Literal[
    "positive",
    "negative",
]


class Expectation(BaseModel):

    category: Category = Field(
        description="Category of the student's expectation."
    )

    sentiment: Sentiment = Field(
        description="Whether the expectation is positive or negative."
    )

    text: str = Field(
        description="The specific expectation expressed by the student."
    )


class ClassificationResult(BaseModel):

    expectations: List[Expectation] = Field(
        description="List of expectations expressed by the student."
    )