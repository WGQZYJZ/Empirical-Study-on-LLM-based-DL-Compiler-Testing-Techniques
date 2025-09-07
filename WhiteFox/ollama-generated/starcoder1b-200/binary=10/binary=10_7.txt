
class Model(torch.nn.Module):
    def __init__(self, other=1):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)

    def forward(self, x1):
        v1 = self.linear(x1)
        return self.linear(v2 + other)


# Inputs to the model
x1 = torch.randn(1, 32, 64)
other = torch.randn(1, 8)
