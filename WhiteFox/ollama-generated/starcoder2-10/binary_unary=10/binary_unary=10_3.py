
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 16, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor
        v3 = relu(v2)
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(5, 4096)
 
# Calling the model and getting the outputs from it
