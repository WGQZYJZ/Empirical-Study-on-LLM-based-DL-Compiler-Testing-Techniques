
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.inp = torch.Tensor([[1, 0], [0, 1]])

    def forward(self, x1, x2=None):
        v1 = x1 + self.inp
        v2 = x1 * 0.5
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
