
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 32)

    def forward(self, x1):
        v0  = self.linear(x1) 
        return clamp(min=0, max=5, v0 + 1).float() * v0


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 64)
