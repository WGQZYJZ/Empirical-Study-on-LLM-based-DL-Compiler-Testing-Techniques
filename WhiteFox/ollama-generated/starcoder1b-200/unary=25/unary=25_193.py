
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)
        self.negative_slope = negative_slope
 
    def forward(self, x):
        v1 = self.linear(x)
        return torch.where(v1 > 0, x, self.negative_slope * v1)

# Initializing the model
m = Model(-2.71828)

# Inputs to the model
x1 = torch.randn(1, 1)
