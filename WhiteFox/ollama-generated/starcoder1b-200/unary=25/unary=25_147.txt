
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0):
        super().__init__()
        self.negative_slope = negative_slope
        self.linear  = torch.nn.Linear(10, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.where(v1 > 0, v1, v1 * self.negative_slope)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
