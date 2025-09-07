
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
        self.add    = torch.nn.Addmm(16, 3, 4, 5, 0)
 
    def forward(self, x):
        v1  = self.linear(x) + other
        return v1


# Inputs to the model
inputs = torch.randn(2, 3, 16, 8)
other   = torch.randn(2, 4, 16, 8)
