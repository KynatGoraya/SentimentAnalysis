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
    - If more than one department is clearly involved based on the Factors, include them all.

**Instructions**:
- Always return a valid JSON object.
- If the review has **both positive and negative parts**, choose the **sdominant sentiment** and mention instigators and factors ** based upon that category only** .
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
            return f"Error: {e}"

    def FewShotsChainOfThought(self, user_review):
        try:
            department_list_string = ", ".join(self.departments)
            prompt = f"""
You are an intelligent sentiment analyzer. Your task is to analyze a patient review and return a structured sentiment analysis in valid JSON. 

**Step-by-Step Chain of Thought Process**:

Step 1: **Read and Understand the Review**
- Carefully read the entire review
- Identify the main topic and context
- Note any emotional language, adjectives, or descriptive phrases

Step 2: **Determine Overall Sentiment**
- Consider the tone and language used
- Weigh positive vs negative expressions
- If mixed sentiments exist, identify which is dominant
- Categorize as Positive, Negative, or Neutral

Step 3: **Extract Key Factors**
- Identify specific complaints, praise, or observations
- Focus on concrete issues or positive aspects mentioned
- Convert sarcastic or figurative language to literal meaning
- List the key factors that support your sentiment classification

Step 4: **Match to Responsible Departments**
- For each factor identified, think about which department would be responsible
- Consider the responsibilities of each department: {department_list_string}
- Only include departments that are directly and reasonably related to the factors
- If unclear or general feedback, use "Unclear" for instigators

**Task Goals**:
1. Categorize the review as **Positive**, **Negative**, or **Neutral** under "Category".
2. List key reasons, complaints, or praise (phrases, adjectives or keywords) to highlight performance — under "Factors" ** based upon the category **.
3. Carefully determine the correct "Instigators" from this list: {department_list_string}. Base this on:
    - A clear understanding of each department's indepth responsibilities aginst patients.
    - Properly match the **Factors** identified to the responsibilities of specific departments to include those departments.
    - Only include a department if it is **reasonably and directly related** to the concern or praise mentioned.
    - **Avoid guessing or hallucinating** a department that is not in the list.
    - **NEVER include departments outside of the list provided**.
    - If more than one department is clearly involved based on the Factors, include them all.

**Instructions**:
- Show your step-by-step reasoning first, then provide the JSON
- Always return a valid JSON object.
- If the review has **both positive and negative parts**, choose the **sdominant sentiment** and mention instigators and factors ** based upon that category only** .
- If the review is **vague** or **lacks detail**, mark it as **Neutral** and use ["General feedback"] for "Factors".
- If the sentiment **targets no one explicitly**, use ["Unclear"] under "Instigators".
- If sarcasm or figurative language is used, interpret the intended meaning and express it in clear, literal terms. For example, rephrase a sarcastic comment like "restrooms with that 'authentic' biohazard aroma" into a straightforward observation such as "restroom smelled awful". Avoid including figurative or sarcastic language directly in the output. 
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

**Examples with Chain of Thought**:

**Input**:
Example 1: Positive Sentiment
User Review:
"Honestly, I didn't expect much after what I'd heard, and the wait time was ridiculous. But once inside, things somehow felt comforting. The nurse seemed a bit lost at first, but she ended up being very kind. The room wasn't perfect, but it had a calming vibe. I still have mixed feelings, but overall, it was better than I imagined."

**Chain of Thought Analysis**:
Step 1 - Reading: This review mentions wait times, nursing care, room conditions, and overall experience.
Step 2 - Sentiment: Despite initial complaints, the dominant sentiment is positive ("comforting", "very kind", "calming vibe", "better than I imagined").
Step 3 - Key Factors: "comforting", "kind", "calming vibe", "better than I imagined" are the positive aspects.
Step 4 - Department Matching: Nursing Department (kind nurse), Inpatient Department (room with calming vibe).

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

**Chain of Thought Analysis**:
Step 1 - Reading: This review contrasts exterior appearance with interior cleanliness issues, mentions bedsheets, restrooms, and medical waste disposal.
Step 2 - Sentiment: Heavily sarcastic and negative, criticizing cleanliness and safety standards.
Step 3 - Key Factors: Converting sarcasm to literal terms: "stained bedsheets", "restroom smelled awful", "used syringes", "infection risks".
Step 4 - Department Matching: Housekeeping (cleaning), Nursing Department (bedsheets/syringes), Inpatient Department (room conditions), Central Sterilization Unit (infection control).

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

**Chain of Thought Analysis**:
Step 1 - Reading: This review expresses uncertainty and ambivalence about the experience, mentions food and doctor interaction.
Step 2 - Sentiment: Neutral - neither particularly positive nor negative, expressing indifference.
Step 3 - Key Factors: Since it's neutral and vague, use "General feedback".
Step 4 - Department Matching: Food mentioned relates to Catering, doctor interaction relates to Outpatient Department.

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

**Chain of Thought Analysis**:
Step 1 - Reading: Very generic hospital visit description with no specific details.
Step 2 - Sentiment: Neutral - no clear positive or negative indicators.
Step 3 - Key Factors: Completely vague, so "General feedback".
Step 4 - Department Matching: No specific department mentioned or implied, so "Unclear".

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

**Now analyze this review with chain of thought**:

Review to analyze: "{user_review}"

**My Chain of Thought Analysis**:
Step 1 - Reading and Understanding:
[Think through what the review is about]

Step 2 - Sentiment Determination:
[Analyze the overall tone and determine if it's positive, negative, or neutral]

Step 3 - Factor Extraction:
[List the specific issues, praise, or observations mentioned]

Step 4 - Department Matching:
[Match each factor to the appropriate department(s) responsible]

**Final JSON Output**:
Return **only** the JSON output above. **Do not include any explanation or commentary**.
"""
            return prompt
        except Exception as e:
            return f"Error: {e}"


 
    def FewShots(self,user_review):
        try:
            department_list_string = ", ".join(self.departments)
            prompt = f"""
You are an intelligent sentiment analyzer. Your task is to analyze a patient review and return a structured sentiment analysis in valid JSON.

**Task Goals**:
1. Categorize the review as **Positive**, **Negative**, or **Neutral** under "Category".
2. List key reasons, complaints, or praise (phrases, adjectives or keywords) to highlight performance — under "Factors" ** based upon the category **.
3. Carefully determine the correct "Instigators" from this list: {department_list_string}. Base this on:
    - A clear understanding of each department's indepth responsibilities aginst patients.
    - Properly match the **Factors** identified to the responsibilities of specific departments to include those departments.
    - Only include a department if it is **reasonably and directly related** to the concern or praise mentioned.
    - **Avoid guessing or hallucinating** a department that is not in the list.
    - **NEVER include departments outside of the list provided**.
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
            return f"Error: {e}"

    def ChainOfThought(self, user_review):
        try:
            department_list_string = ", ".join(self.departments)
            prompt = f"""
You are an intelligent sentiment analyzer. Your task is to analyze a patient review and return a structured sentiment analysis in valid JSON. 

**Step-by-Step Chain of Thought Process**:

Step 1: **Read and Understand the Review**
- Carefully read the entire review
- Identify the main topic and context
- Note any emotional language, adjectives, or descriptive phrases

Step 2: **Determine Overall Sentiment**
- Consider the tone and language used
- Weigh positive vs negative expressions
- If mixed sentiments exist, identify which is dominant
- Categorize as Positive, Negative, or Neutral

Step 3: **Extract Key Factors**
- Identify specific complaints, praise, or observations
- Focus on concrete issues or positive aspects mentioned
- Convert sarcastic or figurative language to literal meaning
- List the key factors that support your sentiment classification

Step 4: **Match to Responsible Departments**
- For each factor identified, think about which department would be responsible
- Consider the responsibilities of each department: {department_list_string}
- Only include departments that are directly and reasonably related to the factors
- If unclear or general feedback, use "Unclear" for instigators

**Task Goals**:
1. Categorize the review as **Positive**, **Negative**, or **Neutral** under "Category".
2. List key reasons, complaints, or praise (phrases, adjectives or keywords) to highlight performance — under "Factors" ** based upon the category **.
3. Carefully determine the correct "Instigators" from this list: {department_list_string}. Base this on:
    - A clear understanding of each department's indepth responsibilities aginst patients.
    - Properly match the **Factors** identified to the responsibilities of specific departments to include those departments.
    - Only include a department if it is **reasonably and directly related** to the concern or praise mentioned.
    - **Avoid guessing or hallucinating** a department that is not in the list.
    - **NEVER include departments outside of the list provided**.
    - If more than one department is clearly involved based on the Factors, include them all.

**Instructions**:
- Show your step-by-step reasoning first, then provide the JSON
- Always return a valid JSON object.
- If the review has **both positive and negative parts**, choose the **sdominant sentiment** and mention instigators and factors ** based upon that category only** .
- If the review is **vague** or **lacks detail**, mark it as **Neutral** and use ["General feedback"] for "Factors".
- If the sentiment **targets no one explicitly**, use ["Unclear"] under "Instigators".
- If sarcasm or figurative language is used, interpret the intended meaning and express it in clear, literal terms. For example, rephrase a sarcastic comment like "restrooms with that 'authentic' biohazard aroma" into a straightforward observation such as "restroom smelled awful". Avoid including figurative or sarcastic language directly in the output. 
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

**Examples with Chain of Thought**:

**Input**:
Example 1: Positive Sentiment
User Review:
"Honestly, I didn't expect much after what I'd heard, and the wait time was ridiculous. But once inside, things somehow felt comforting. The nurse seemed a bit lost at first, but she ended up being very kind. The room wasn't perfect, but it had a calming vibe. I still have mixed feelings, but overall, it was better than I imagined."

**Chain of Thought Analysis**:
Step 1 - Reading: This review mentions wait times, nursing care, room conditions, and overall experience.
Step 2 - Sentiment: Despite initial complaints, the dominant sentiment is positive ("comforting", "very kind", "calming vibe", "better than I imagined").
Step 3 - Key Factors: "comforting", "kind", "calming vibe", "better than I imagined" are the positive aspects.
Step 4 - Department Matching: Nursing Department (kind nurse), Inpatient Department (room with calming vibe).

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

**Chain of Thought Analysis**:
Step 1 - Reading: This review contrasts exterior appearance with interior cleanliness issues, mentions bedsheets, restrooms, and medical waste disposal.
Step 2 - Sentiment: Heavily sarcastic and negative, criticizing cleanliness and safety standards.
Step 3 - Key Factors: Converting sarcasm to literal terms: "stained bedsheets", "restroom smelled awful", "used syringes", "infection risks".
Step 4 - Department Matching: Housekeeping (cleaning), Nursing Department (bedsheets/syringes), Inpatient Department (room conditions), Central Sterilization Unit (infection control).

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

**Chain of Thought Analysis**:
Step 1 - Reading: This review expresses uncertainty and ambivalence about the experience, mentions food and doctor interaction.
Step 2 - Sentiment: Neutral - neither particularly positive nor negative, expressing indifference.
Step 3 - Key Factors: Since it's neutral and vague, use "General feedback".
Step 4 - Department Matching: Food mentioned relates to Catering, doctor interaction relates to Outpatient Department.

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

**Chain of Thought Analysis**:
Step 1 - Reading: Very generic hospital visit description with no specific details.
Step 2 - Sentiment: Neutral - no clear positive or negative indicators.
Step 3 - Key Factors: Completely vague, so "General feedback".
Step 4 - Department Matching: No specific department mentioned or implied, so "Unclear".

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

**Now analyze this review with chain of thought**:

Review to analyze: "{user_review}"

**My Chain of Thought Analysis**:
Step 1 - Reading and Understanding:
[Think through what the review is about]

Step 2 - Sentiment Determination:
[Analyze the overall tone and determine if it's positive, negative, or neutral]

Step 3 - Factor Extraction:
[List the specific issues, praise, or observations mentioned]

Step 4 - Department Matching:
[Match each factor to the appropriate department(s) responsible]

**Final JSON Output**:
Return **only** the JSON output above. **Do not include any explanation or commentary**.
"""
            return prompt
        except Exception as e:
            return f"Error: {e}"
