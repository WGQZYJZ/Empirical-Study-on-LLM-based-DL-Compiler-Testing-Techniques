
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8192, 4096)
 
    def forward(self, x):
        v1  = self.linear(x) 
        v2  = v1 - other # Substracting 'other' from the result
        v3  = torch.relu(v2) # Apply the ReLU function to the result of subtraction
        return v3

# Initializing and compiling a model
m = Model()


# Inputs to the model
x  = torch.randn(1, 8192)
__output__  = m(x)
