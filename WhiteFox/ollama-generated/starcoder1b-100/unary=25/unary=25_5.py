
class Model(torch.nn.Module):
    def __init__(self, positive_slope):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)
        self.positive_slope = positive_slope
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0
        v3 = (self.positive_slope * v1).view(v1.shape[0], -1)
        return torch.where(v2, v1, v3)


# Initializing the model
m = Model(0.5)


