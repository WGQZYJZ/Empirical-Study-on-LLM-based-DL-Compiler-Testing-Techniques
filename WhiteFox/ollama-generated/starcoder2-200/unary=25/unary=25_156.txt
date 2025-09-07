
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 48)
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0
        v2 = -0.5 if x1 < 0 else x1
        v3 = v1 * negative_slope
        return torch.where(v2, v1, v3)


# Initializing the model
m = Model()
negative_slope = 0.5
 
# Inputs to the model
x1 = torch.randn(48, 32)