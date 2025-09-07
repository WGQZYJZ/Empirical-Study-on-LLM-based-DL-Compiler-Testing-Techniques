
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 3
        v2 = torch.clamp_min(v1, 0)
        v3 = torch.clamp_max(v2, 6)
        return v3 / 6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 5)
