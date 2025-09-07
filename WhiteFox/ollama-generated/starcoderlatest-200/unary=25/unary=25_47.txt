
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0
        v2 = v1 * negative_slope
        v3 = torch.where(v1, v2, v1)
        return v3


# Inputs to the model
x1 = torch.randn(4, 1, 64, 64)
