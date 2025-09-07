
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(64, 8)
        self.negative_slope  = 0.2
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2  = (v1 > 0).float() * v1 + (~(v1 > 0).float()) * (-self.negative_slope * v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 64)
