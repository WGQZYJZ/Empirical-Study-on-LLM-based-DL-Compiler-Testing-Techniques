
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = clamp(min=0, max=6, l1 + 3) * 0.7845612626029625 # Multiply the output of the linear transformation by the clamped output of the linear transformation added with 3
        v3 = v1 / 6
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 10)
