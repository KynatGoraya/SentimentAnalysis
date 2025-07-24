class Prompts:
    def __init__(self):
        self.departments = [
            "Casualty Department", "Operating Theatre", "Intensive Care Unit", "Anesthesiology Department",
            "Cardiology Department", "ENT Department", "Geriatric Department", "Gastroenterology Department",
            "General Surgery", "Gynaecology Department", "Haematology Department", "Pediatrics Department",
            "Neurology Department", "Oncology Department", "Ophthalmology Department", "Orthopaedic Department",
            "Urology Department", "Psychiatry Department", "Inpatient Department", "Outpatient Department",
            "Nursing Department", "Pharmacy Department", "Radiology Department", "Clinical Pathology Department",
            "Nutrition and Dietetics", "Catering and Food Services", "Central Sterilization Unit", "Housekeeping",
            "Clinical Engineering Department", "Information Technology and Communication", "Engineering Services",
            "Medical Records Department", "Human Resources Department", "Finance Department", "Administrative Department"
        ]

    def ZeroShot(self,user_review):
        try:
            department_list_string = ", ".join(self.departments)
            prompt = f"""
You are an intelligent sentiment analyzer. Your task is to analyze a patient review and return a structured sentiment analysis in valid JSON.

**Task Goals**:
1. Categorize the review as **Positive**, **Negative**, or **Neutral** under "Category".
2. List key reasons, complaints, or praise (phrases or keywords) to highlight performance — under "Factors" ** based upon the category **.
3. Carefully determine the correct "Instigators" from this list: {department_list_string}. Base this on:
    - A clear understanding of each department's indepth responsibilities aginst patients.
    - Properly match the **Factors** identified to the responsibilities of specific departments to include those departments.
    - Only include a department if it is **reasonably and directly related** to the concern or praise mentioned.
    - Avoid guessing or hallucinating. 
    - **NEVER** include departments outside of the list provided.
    - If the patient mentions a department not present in the provided list, infer its meaning based on context and map it to the closest matching department by responsibility.
    - If more than one department is clearly involved based on the Factors, include them all.

**Instructions**:
- Always return a valid JSON object.
- If the review has **both positive and negative parts**, choose the **dominant sentiment** and mention instigators and factors ** based upon that category only** .
- If the review is **vague** or **lacks detail**, mark it as **Neutral** and use ["General feedback"] for "Factors".
- If the sentiment **targets no one explicitly**, use ["Unclear"] under "Instigators".
- If sarcasm or figurative language is used, interpret the intended meaning and express it in clear, literal terms.
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
            return f"Error generating prompt: {e}"
 
 # if i add adjectives in the factors; it lists adjectives to express the sentiment
    def FewShots(self,user_review):
        try:
            department_list_string = ", ".join(self.departments)
            prompt = f"""
You are an intelligent sentiment analyzer. Your task is to analyze a patient review and return a structured sentiment analysis in valid JSON.

**Task Goals**:
1. Categorize the review as **Positive**, **Negative**, or **Neutral** under "Category".
2. List key reasons, complaints, or praise (phrases or keywords) to highlight performance — under "Factors" ** based upon the category **.
3. Carefully determine the correct "Instigators" from this list: {department_list_string}. Base this on:
    - A clear understanding of each department's indepth responsibilities aginst patients.
    - Properly match the **Factors** identified to the responsibilities of specific departments to include those departments.
    - Only include a department if it is **reasonably and directly related** to the concern or praise mentioned.
    - **Avoid guessing or hallucinating** a department that is not in the list.
    - **NEVER include departments outside of the list provided**.
    - If the patient mentions a department not present in the provided list, infer its meaning based on context and map it to the closest matching department by responsibility.
    - Like if the patient says " Billing department was awful"; the alternative to Billing department is "Finance Department" in the pre-mentioned list studied based upon responisiblities.
    - If more than one department is clearly involved based on the Factors, include them all.

**Instructions**:
- Always return a valid JSON object.
- If the review has **both positive and negative parts**, choose the **sdominant sentiment** and mention instigators and factors ** based upon that category only** .
- If the review is **vague** or **lacks detail**, mark it as **Neutral** and use ["General feedback"] for "Factors".
- If the sentiment **targets no one explicitly**, use ["Unclear"] under "Instigators".
- If sarcasm or figurative language is used, interpret the intended meaning and express it in clear, literal terms. For example, rephrase a sarcastic comment like "restrooms with that 'authentic' biohazard aroma" into a straightforward observation such as "restroom smelled awful". Avoid including figurative or sarcastic language directly in the output. 
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
        "Instigators": [
            "Nursing Department",
            "Inpatient Department"
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
        "Instigators": [
            "Housekeeping",
            "Nursing Department",
            "Inpatient Department",
            "Central Sterilization Unit"
        ],
        "Factors": [
            "stained bedsheets",
            "restroom smelled awful",
            "used syringes",
            "infection risks"
        ]
    }}
}}

**Input**:
Example 3: Neutral Sentiment
User Review:
 "I guess things went as expected, which is either good or just average. No one really stood out, but no one messed up either. The food looked weird but tasted fine, and the doctor didn't say much — maybe that's just how he is. I'm not really sure what to make of it all."
**Output**:
 ```json
 {{
        "Sentiment Analysis": {{
            "Category": [
                "Neutral"
            ],
            "Instigators": [
                "Catering and Food Services",
                "Outpatient Department"
            ],
            "Factors": [
                "General feedback"
            ]
        }}
}}

**Input**:
Example 4: Neutral Sentiment
User Review:
"It was a hospital visit like any other. I waited, got what I came for, and left. Nothing really stood out to me — good or bad. Just another day, I suppose."
 **Output**:
 ```json
 {{
    "Sentiment Analysis": {{
        "Category":["Neutral"],
        "Instigators": [
            "Unclear"
        ],
        "Factors": [
            "General feedback"
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
        department_list_string = ", ".join(self.departments)
        try:
            prompt=f"""
You are an intelligent sentiment analyzer. Your task is to analyze a patient review and return ** only ** a structured sentiment analysis in valid JSON. Below is a step-by-step chain-of-thought approach to guide you through the process.

**Step-by-Step Chain of Thought**:

1. **Understand the Review**:
   - Read the user review carefully and thouroughly: "{user_review}".
   - Identify the overall tone by looking for emotionally charged words, phrases, or descriptions (e.g., "kind," "awful," "comforting").
   - Detect any sarcasm or figurative language (e.g., "restrooms with that 'authentic' biohazard aroma").  

2. **Determine the Dominant Sentiment**:
   - Categorize the review as **Positive**, **Negative**, or **Neutral** based on the dominant tone.
   - If the review contains more than one sentiment, focus on the **stronger sentiment** (e.g., more emphasis on praise or complaints) to assign the category.
   - If the review is vague, lacks detail, or expresses indifference, classify it as **Neutral**.
   - **List the sentiment identified under the ** Category ** element of the JSON.**

3. **Identify Factors**:
   - Extract key phrases, or keywords that explain the sentiment included in the Category(e.g., "kind nurse," "stained bedsheets," "calming vibe").
   - Add them to the ** Factors ** element of JSON format.
   - For **Neutral** reviews, if no specific factors are clear, use ["General feedback"].
   - If the review includes sarcasm, rewrite those phrases into direct, literal expressions. For example, instead of "used syringes as part of the décor near the waste bin," use "used syringes found near the waste bin."

4. **Assign Instigators**:
   - Use this list **only** for departments: {department_list_string}.
   - Think about the responsiblities and duties of each department against patients.
   - Match the identified **Factors** to the responsibilities of specific departments properly and include those departments only.
   - If no department is clearly tied to the factors, use ["Unclear"].
   - **Never include departments outside the provided list** or guess departments not mentioned.
   - If the patient mentions a department not present in the provided list, infer its meaning based on context and map it to the closest matching department by responsibility.
   - Like if the patient says " Billing department was awful"; the alternative to Billing department is "Finance Department" in the pre-mentioned list studied based upon responisiblities.
   - List the departments under the ** Instigators ** element of JSON.

5. **Structure the Output**:
    -Always return only a valid JSON Format.
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
Example:
This what the entire flow looks like and how the output shows on the user end on postman.
**Input**:
Example 4: Neutral Sentiment
User Review:
"It was a hospital visit like any other. I waited, got what I came for, and left. Nothing really stood out to me — good or bad. Just another day, I suppose."
 **Output**:
 ```json
 {{
    "Sentiment Analysis": {{
        "Category":["Neutral"],
        "Instigators": [
            "Unclear"
        ],
        "Factors": [
            "General feedback"
        ]
    }}
}}
        """
            return prompt
        except Exception as e:
            return f"Error generating prompt: {e}"