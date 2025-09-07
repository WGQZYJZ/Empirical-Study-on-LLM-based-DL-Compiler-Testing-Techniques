
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor = 0):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.other   = other
 
    def forward(self, x1):
        v1 = self.linear(x1) + self.other
        return relu(v1)


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
