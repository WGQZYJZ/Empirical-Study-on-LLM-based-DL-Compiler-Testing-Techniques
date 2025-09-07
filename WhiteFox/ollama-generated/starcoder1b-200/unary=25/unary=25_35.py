
class Model(torch.nn.Module):
    def __init__(self, negative_slope=1e-2):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x):
        v = self.linear(x)
        v = torch.where(v > 0, v, -v * self.negative_slope)
        return v


# Inputs to the model
x1 = torch.randn(1, 3)
