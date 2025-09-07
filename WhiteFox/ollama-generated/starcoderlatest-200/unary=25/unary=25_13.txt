
class Model(torch.nn.Module):
    def __init__(self, slope=1e-2):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.negative_slope = slope
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
