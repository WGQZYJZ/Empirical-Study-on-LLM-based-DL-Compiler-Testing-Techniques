
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 32)
        self.negative_slope = 0.01
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0
        v2 = v1 * self.negative_slope
        v3 = torch.where(v1, x1, v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 128)
