
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 8)
        self.negative_slope = .2
 
    def forward(self, x0):
        v0 = self.linear(x0)
        v1 = v0 > 0
        v3 = v0 * negative_slope
        v4 = torch.where(v1, v0, v3)
        return v4


# Initializing the model
m  = Model()
