
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 8)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.where(v1 > 0, v1, (self.negative_slope * v1))
        return v2


# Initializing the model
m = Model(negative_slope=0.25)


