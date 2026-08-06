class LLMModel:
    # 1. The Constructor: Initializes the object's starting data
    def __init__(self, name, parameters):
        self.name = name           # Attribute
        self.parameters = parameters # Attribute

    # 2. A Method: An action the object can perform
    def describe(self):
        return f"Model: {self.name}, Size: {self.parameters}"

# 3. Creating an Object (Instantiating the class)
my_ai = LLMModel("Llama-3", "8B")

# 4. Accessing attributes and calling methods
print(my_ai.name)           # Output: Llama-3
print(my_ai.describe())     # Output: Model: Llama-3, Size: 8B