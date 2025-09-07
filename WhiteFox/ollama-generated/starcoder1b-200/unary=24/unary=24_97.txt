
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float = 0.25):
        super().__init__()
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = x1 > 0
        v2 = torch.where(v1, x1, -self.negative_slope * x1)
        return v2


# Initializing the model
m = Model()


