
class Model(torch.nn.Module):
    def __init__(self, min_value = 10., max_value = 238974):
        super().__init__()
        self.linear = torch.nn.Linear(64*64*3, 1)
 
    def forward(self, x1): 
        v1 = self.linear(x1.flatten())
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
input_tensor=torch.randn(64*64*3).reshape((1,) + (64, 64, 3))
__output__= m(input_tensor) # Model's output on inputs

System: You are a source code analyzer for PyTorch.

User: 