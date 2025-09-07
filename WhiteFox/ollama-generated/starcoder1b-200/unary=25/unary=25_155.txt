
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
 
    def forward(self, x):
        v = self.linear(x)
        return torch.where(v > 0, v, -(v + 1))


# Inputs to the model
x1 = torch.randn(2, 8)
