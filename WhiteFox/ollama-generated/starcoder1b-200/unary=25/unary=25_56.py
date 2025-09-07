
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).float() * v1
        v3 = negative_slope * v1
        v4 = (v1 * v3 < 0).float() * v1 + negative_slope * v3
        return torch.where(v2, x1, v4)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8)
