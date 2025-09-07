
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.where(v1 > 0, v1, negative_slope * v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 1, 64, 64)
