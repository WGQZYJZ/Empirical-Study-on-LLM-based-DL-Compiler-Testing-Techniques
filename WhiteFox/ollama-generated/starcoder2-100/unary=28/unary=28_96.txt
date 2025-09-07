
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)

        v2 = torch.clamp_min(v1, min=-9376.45703125)
        v3 = torch.clamp_max(v2, max=8200544.0)
        return v3

# Initializing the model
m  = Model()
x1  = torch.randn(2, 10)

 # Inputs to the model
 __output__  = m(x1)

System: You are a source code analyzer for PyTorch.

User: 