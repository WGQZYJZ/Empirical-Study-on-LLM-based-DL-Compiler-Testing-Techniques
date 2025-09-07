
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 10)
 
    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v2


# Inputs to the model
x1 = torch.randn(1, 2, 4)
other = torch.randn(1, 3)
