
class Model(torch.nn.Module):
    def __init__(self, other=2.0):
        super().__init__()
        self.linear = torch.nn.Linear(3, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v2


# Inputs to the model
x1 = torch.randn(1, 3)
other = 4.0
