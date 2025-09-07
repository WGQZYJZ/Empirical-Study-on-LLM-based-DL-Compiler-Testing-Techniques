
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float = 0.25):
        super().__init__()
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = torch.relu(x1)
        v2 = torch.where(torch.gt(v1, 0), x1 * self.negative_slope, x1)
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
