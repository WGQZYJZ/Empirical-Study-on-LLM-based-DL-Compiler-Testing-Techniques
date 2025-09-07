
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.linear = torch.nn.Linear(16, 32)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.where(v1 > 0, v1, -self.negative_slope * v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 16)
