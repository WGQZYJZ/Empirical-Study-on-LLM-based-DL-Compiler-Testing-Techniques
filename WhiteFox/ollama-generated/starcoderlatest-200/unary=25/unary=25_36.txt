
class Model(torch.nn.Module):
    def __init__(self, neg_slope: float = 0.01):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self._neg_slope = neg_slope
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).float()
        v3 = v1 * -self._neg_slope
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m = Model(neg_slope=0.01)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
