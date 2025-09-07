
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if other is not None:
            return v1 + other
        return v1

# Initializing the model
m2 = Model2()

# Inputs to the model
x2 = torch.randn(1, 3, 64, 64)
other_tensor = torch.randn(1, 8, 1)
__output2__ = m2(x2, other=other_tensor)

