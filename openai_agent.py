import openai
import json

openai.api_key = "your-api-key"  # ideally use environment variables

def query_openai_for_diversity(insight_dict):
    system_prompt = """
    You are a helpful data assistant trained to analyze dataset fairness and diversity.
    Based on the input data summary below, identify:
    - Any imbalanced categorical columns
    - Underrepresented groups
    - Suggestions to improve representation
    Be specific and objective in your feedback.
    """

    user_prompt = f"Here is the summary:\n{json.dumps(insight_dict, indent=2)}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.5
    )

    return response.choices[0].message["content"]