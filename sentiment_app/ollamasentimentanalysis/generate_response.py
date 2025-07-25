# generate_response.py
import ollama

class GenerateResponse:
    def __init__(self, model_name="gemma3:latest"):
        try:
            self.model = model_name
        except Exception as e:
            raise Exception("Error finding model {model_name}",e)

    def check_ollama_model(self):
        print("checking")
        try:
            #print("checking 2")
            models = ollama.list()
            print(models)
            model_names = [model.model for model in models['models']]
            print("Printing model names",model_names)
            if self.model not in model_names:
                print(f"Model '{self.model}' not found. Pull it before using")
            else:
                print(f"Model '{self.model}' is already available.")
            response = ollama.chat(
                model=self.model,
                messages=[{"role": "user", "content": "Say Hello"}]
            )
            print("Ollama is working. Sample response:")
            print(response['message']['content'])

        except Exception as e:
            print("Error during Ollama model check:", e)

    def getresponse(self, prompt):
        self.check_ollama_model()
        try:
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
