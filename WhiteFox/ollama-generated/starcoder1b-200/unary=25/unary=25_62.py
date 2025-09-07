
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        return torch.where(x1 > 0, x1, -self.negative_slope * x1)


# Initializing the model
m = Model(-3)


