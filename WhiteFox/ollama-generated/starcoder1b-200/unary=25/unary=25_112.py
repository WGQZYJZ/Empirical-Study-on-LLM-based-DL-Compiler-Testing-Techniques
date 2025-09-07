
class Model(torch.nn.Module):
    def __init__(self, positive_slope):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 8)
        self.positive_slope = positive_slope
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2 = v1 > 0
        v3 = v1 * self.positive_slope
        v4 = torch.where(v2, v1, v3)
        return v4


# Inputs to the model
__inputs__ = torch.randn(1, 8)
