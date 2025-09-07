
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 256, 10)
 
    def forward(self, x1):
        return self.linear(x1 + other)


# Inputs to the model
x1 = torch.randn(1, 3, 256, 1)
