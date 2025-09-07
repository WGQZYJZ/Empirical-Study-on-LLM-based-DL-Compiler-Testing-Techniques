
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 4)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if other is None:
            pass
        else:
            v2 = v1 + other
        return v2


# Initializing the model
m = Model2()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.randn(1, 4, 64, 64)
