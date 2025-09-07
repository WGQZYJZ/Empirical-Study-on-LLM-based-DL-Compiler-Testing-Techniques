
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 * clamp(min=0, max=6, v1 + 3)
        return v2 / 6


m  = Model()
__output__  = m(torch.randn(1, 3))

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3)

# Outputs from the model
