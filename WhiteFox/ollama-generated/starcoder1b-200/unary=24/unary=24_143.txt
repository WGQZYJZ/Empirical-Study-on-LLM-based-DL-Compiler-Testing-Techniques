
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float):
        super().__init__()
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = torch.where(x1 > 0, x1 * self.negative_slope, x1)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
