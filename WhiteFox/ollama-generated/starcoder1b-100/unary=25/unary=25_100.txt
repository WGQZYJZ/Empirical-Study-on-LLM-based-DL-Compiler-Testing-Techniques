
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0
        v2 = (x1 * -self.negative_slope).floor()
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
