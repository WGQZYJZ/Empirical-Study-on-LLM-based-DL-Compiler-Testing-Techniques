
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.l1(x1)
        v2 = torch.clamp(v1 * (v1 + 3), min=0, max=6) / 6
        return v2


# Initializing the model
m2 = Model2()

# Inputs to the model
x2 = torch.randn(1, 3, 64, 64)
