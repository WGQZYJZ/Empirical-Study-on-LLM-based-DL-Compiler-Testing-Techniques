
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        if other is None:
            self.linear = torch.nn.Linear(3, 8)
        else:
            self.linear = torch.nn.Linear(3, 8, bias=True)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        if other is not None:
            v2 = v1 + other
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.randn(8, dtype=torch.float)
