
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 * ((-1) * torch.clamp((3 + abs(v1)) / 6, min=0)).round() + 1).div(6)
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 5)
