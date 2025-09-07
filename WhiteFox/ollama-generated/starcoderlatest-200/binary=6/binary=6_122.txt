
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 0.75
        return v2


# Inputs to the model
x1 = torch.randn(256, 32, 32)
