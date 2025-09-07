
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = v1 - other_tensor  # other_tensor is a variable that can be found in the global variables and its value is -0.5.
        v3 = torch.nn.functional.relu(v2) 
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 2)
__output__  = m(x1)

