
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float = 1e-3):
        super().__init__()
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = torch.abs(x1) > 0
        v2 = self.negative_slope * (v1 - x1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
