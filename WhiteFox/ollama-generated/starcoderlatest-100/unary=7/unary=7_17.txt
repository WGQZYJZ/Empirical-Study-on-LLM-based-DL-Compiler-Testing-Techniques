
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = clamp(min=0, max=6, v1 + 3) / 6
        return v2


# Initializing the model
m = Model2()

# Inputs to the model
x2 = torch.randn(1, 8, 64, 64)
