
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float = 1.0):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.where(v1 > 0, v1, self.negative_slope * v1)  # For each element in v1 where v1[i] > 0, choose the corresponding element from the output of the linear transformation of x1[i], otherwise choose the corresponding element from the multiplication by the negative slope of the output of the linear transformation of x1[i]
        return v2


# Inputs to the model
x1 = torch.randn(1, 3)
