
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.01):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return torch.where(v1 > 0, v1, -self.negative_slope * v1)


# Initializing the model
m = Model()


