# generate_response.py
import ollama

class GenerateResponse:
    def __init__(self, model_name="gemma3"):
        try:
            self.model = model_name
        except Exception as e:
            raise Exception("Error finding model {model_name}",e)

    def check_ollama_model(self):
        try:
            models = ollama.list()
            model_names = [model['name'] for model in models['models']]

            if self.model not in model_names:
                print(f"Model '{self.model}' not found. Attempting to pull it...")
                ollama.pull(self.model)
                print(f"Successfully pulled '{self.model}'")

            else:
                print(f"Model '{self.model}' is already available.")
            response = ollama.chat(
                model=self.model,
                messages=[{"role": "user", "content": "Hello"}]
            )
            print("Ollama is working. Sample response:")
            print(response['message']['content'])

        except Exception as e:
            print("Error during Ollama model check:", e)

    def getresponse(self, prompt):
        try:
            self.check_ollama_model()
            response = ollama.chat(
                model=self.model,
                messages=[
                    {
                    "role": "user", 
                    "content": prompt
                    }
                ]
            )
            result = response['message']['content']
            #print(result)
            return result
        except Exception as e:
            raise Exception("Error generating response:", e)
