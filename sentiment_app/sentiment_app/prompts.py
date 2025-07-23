class Prompts:
    def ZeroShot(self,user_review):
        try:
            prompt = f"""
You are an intelligent sentiment analyzer. Your task is to analyze a patient review and return a structured sentiment analysis in valid JSON.

**Task Goals**:
1. Categorize the review as **Positive**, **Negative**, or **Neutral** under "Category".
2. Identify who the target is based on the category: **Hospital**, ** Doctors ** , **Staff** — under "Instigators". If there are more than one insitgatoes based upon the category, add them both under the instigators.
3. List key reasons, complaints, or praise (phrases, adjectives or keywords) to highlight performance — under "Factors" ** based upon the category **.

**Instructions**:
- Always return a valid JSON object.
- If the review has **both positive and negative parts**, choose the **dominant sentiment** and mention instigators and factors ** based upon that category only** .
- If the review is **vague** or **lacks detail**, mark it as **Neutral** and use ["General feedback"] for "Factors".
- If the sentiment **targets no one explicitly**, use ["Unclear"] under "Instigators".
- If sarcasm or figurative language is used, **infer the intended meaning**.
- NEVER include explanation, commentary, or anything outside of the JSON.
- All JSON fields must be non-empty arrays (strings inside arrays).

**Output Format**:
```json
{{
  "Sentiment Analysis": {{
    "Category": ["<<category>>"],
    "Instigators": ["<<instigators>>"],
    "Factors": ["<<factors>>"]
  }}
}}

Analyze the following user review: "{user_review}"

Return **only** the JSON output above. **Do not include any explanation or commentary**.
"""

            return prompt
        except Exception as e:
            return f"Error: {e}"
