
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float = 0.1):
        super().__init__()
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = torch.where(x1 > 0, 2 * x1 - 1, x1)
        return v1 * self.negative_slope


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
