
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x1, min_value=0.5, max_value=2.0):
        v1 = self.linear(x1)
        v2 = v1 * torch.clamp(min_value, min_value - 1e-6)
        v3 = v2 * torch.clamp(max_value, max_value + 1e-6)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
