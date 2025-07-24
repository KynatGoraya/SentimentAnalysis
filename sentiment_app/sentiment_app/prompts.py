class Prompts:
    # def __init__(self):
        # self.departments = [
        #     "Casualty Department", "Operating Theatre", "Intensive Care Unit", "Anesthesiology Department",
        #     "Cardiology Department", "ENT Department", "Geriatric Department", "Gastroenterology Department",
        #     "General Surgery", "Gynaecology Department", "Haematology Department", "Pediatrics Department",
        #     "Neurology Department", "Oncology Department", "Ophthalmology Department", "Orthopaedic Department",
        #     "Urology Department", "Psychiatry Department", "Inpatient Department", "Outpatient Department",
        #     "Nursing Department", "Pharmacy Department", "Radiology Department", "Clinical Pathology Department",
        #     "Nutrition and Dietetics", "Catering and Food Services", "Central Sterilization Unit", "Housekeeping",
        #     "Clinical Engineering Department", "Information Technology and Communication", "Engineering Services",
        #     "Medical Records Department", "Human Resources Department", "Finance Department", "Administrative Department"
        # ]

    def ZeroShot(self,user_review):
        try:
            #department_list_string = ", ".join(self.departments)
            prompt = f"""
You are an intelligent sentiment analyzer. Your task is to analyze a patient review and return a structured sentiment analysis in valid JSON.

**Task Goals**:
1. Categorize the review as **Positive**, **Negative**, or **Neutral** under "Category".
2. List theme based adjectives to highlight performance — under "Factors" ** based upon the category **.
**Instructions**:
- Always return a valid JSON object.
- If sarcasm or figurative language is used, interpret the intended meaning and express it in clear, literal terms.
- NEVER include explanation, commentary, or anything outside of the JSON.
- All JSON fields must be non-empty arrays (strings inside arrays).
**Output Format**:
```json
{{
  "Sentiment Analysis": {{
    "Category": ["<<category>>"],
    "Factors": ["<<factors>>"]
  }}
}}

Analyze the following user review: "{user_review}"

Return **only** the JSON output above. **Do not include any explanation or commentary**.
"""

            return prompt
        except Exception as e:
            return f"Error generating prompt: {e}"
 
 
    def FewShots(self,user_review):
        try:
           # department_list_string = ", ".join(self.departments)
            prompt = f"""
You are an intelligent sentiment analyzer. Your task is to analyze a patient review and return a structured sentiment analysis in valid JSON.

**Task Goals**:
1. Categorize the review as **Positive**, **Negative**, or **Neutral** under "Category".
2. List  theme based adjectives to highlight performance — under "Factors" ** based upon the category **.
**Instructions**:
- Always return a valid JSON object. 
- If sarcasm or figurative language is used, interpret the intended meaning and express it in clear, literal terms. For example, rephrase a sarcastic comment like "restrooms with that 'authentic' biohazard aroma" into a straightforward observation such as "restroom smelled awful". Avoid including figurative or sarcastic language directly in the output. 
- NEVER include explanation, commentary, or anything outside of the JSON.
- All JSON fields must be non-empty arrays (strings inside arrays).

**Output Format**:
```json
{{
  "Sentiment Analysis": {{
    "Category": ["<<category>>"],
    "Factors": ["<<factors>>"]
  }}
}}
**Input**:
Example 1: Positive Sentiment
User Review:
"Honestly, I didn't expect much after what I'd heard, and the wait time was ridiculous. But once inside, things somehow felt comforting. The nurse seemed a bit lost at first, but she ended up being very kind. The room wasn't perfect, but it had a calming vibe. I still have mixed feelings, but overall, it was better than I imagined."
**Output**:
```json
 {{
    "Sentiment Analysis": {{
        "Category": [
            "Positive"
        ],
        "Factors": [
            "comforting",
            "kind",
            "calming vibe",
            "better than I imagined"
        ]
    }}
}}

**Input**:
Example 2: Negative Sentiment
User Review:
 "The hospital's exterior was spotless — you'd think you were walking into a five-star hotel. But step inside, and it's a different story. Stained bedsheets, restrooms with that 'authentic' biohazard aroma, and used syringes as part of the décor near the waste bin. Truly a masterclass in infection control — I felt so 'safe' I almost asked for a second room."
 **Output**:
 ```json
 {{
    "Sentiment Analysis": {{
        "Category": [
            "Negative"
        ],
        "Factors": [
            "stained bedsheets",
            "restroom smelled awful",
            "used syringes",
            "infection risks"
        ]
    }}
}}
Analyze the following user review: "{user_review}"

Return **only** the JSON output above. **Do not include any explanation or commentary**.
"""

            return prompt
        except Exception as e:
            return f"Error generating prompt: {e}"
        
    def ChainOfThought(self,user_review):
        #department_list_string = ", ".join(self.departments)
        try:
            prompt=f"""
You are an intelligent sentiment analyzer. Your task is to analyze a patient review and return ** only ** a structured sentiment analysis in valid JSON. Below is a step-by-step chain-of-thought approach to guide you through the process.

**Step-by-Step Chain of Thought**:

1. **Understand the Review**:
   - Read the user review carefully and thouroughly: "{user_review}" and identify overall tone.

2. **Determine the Dominant Sentiment**:
   - Categorize the review as one of these: **Positive**, **Negative**, or **Neutral** based on the ** dominent, stronger sentiment **.
   - **List the sentiment identified under the ** Category ** element of the JSON.**

3. **Identify **Factors** **:
   - Extract theme based adjectives that explain the sentiment included in the Category.
   - Add them to the ** Factors ** element of JSON format.
   - If the review includes sarcasm, rewrite those phrases into direct, literal expressions. For example, instead of "used syringes as part of the décor near the waste bin," use "used syringes found near the waste bin."
4. **Structure the Output**:
    -Always return only a valid JSON Format.
    - NEVER include explanation, commentary, or anything outside of the JSON.
    - All JSON fields must be non-empty arrays (strings inside arrays).
**Output Format**:
```json
{{
  "Sentiment Analysis": {{
    "Category": ["<<category>>"],
    "Factors": ["<<factors>>"]
  }}
}}      """
            return prompt
        except Exception as e:
            return f"Error generating prompt: {e}"