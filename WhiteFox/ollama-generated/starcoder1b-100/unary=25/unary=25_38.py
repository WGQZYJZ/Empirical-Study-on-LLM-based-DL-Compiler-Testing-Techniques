
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0):
        super().__init__()
        self.linear = torch.nn.Linear(32, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0
        v2 = self.linear(x1) * negative_slope
        v3 = torch.where(v2, x1, v2)
        return v3


# Inputs to the model
x1 = torch.randn(1, 32)
