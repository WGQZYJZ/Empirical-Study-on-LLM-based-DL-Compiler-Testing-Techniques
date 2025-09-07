
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
        self.other = other
 
    def forward(self, x1):
        v1 = self.linear(x1) + self.other
        return v1


# Inputs to the model
x1 = torch.randn(1, 8)
other = torch.randn(32)
