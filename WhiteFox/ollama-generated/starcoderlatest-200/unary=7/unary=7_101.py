
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 16)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = clamp_l1(v1, 0, 6) * v1 + 3
        v3 = v2 / 6
        return v3


# Initializing the model
m2 = Model2()


# Inputs to the model
x2 = torch.randn(1, 3, 64, 64)
__output2__ = m2(x2)

