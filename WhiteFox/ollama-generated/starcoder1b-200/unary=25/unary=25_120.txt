
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 8)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0
        v2 = v1 * (-1.0*self.negative_slope)
        v3 = torch.where(v2, x1, self.negative_slope*x1)
        return v3


# Initializing the model
m = Model()

