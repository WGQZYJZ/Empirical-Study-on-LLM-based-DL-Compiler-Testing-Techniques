
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = self.linear(x2)
        return v2


# Inputs to the model
x1 = torch.randn(1, 2, 2)
__output_A__ = m(x1)
x2 = torch.randn(1, 2, 2)
__output_B__ = m(x2)

