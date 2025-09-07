
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0):
        super().__init__()
        self.linear  = torch.nn.Linear(20, 4)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0
        return (torch.where(v1, x1 * -self.negative_slope, v1 * 2)).clamp(min=0)


# Initializing the model
m = Model()


