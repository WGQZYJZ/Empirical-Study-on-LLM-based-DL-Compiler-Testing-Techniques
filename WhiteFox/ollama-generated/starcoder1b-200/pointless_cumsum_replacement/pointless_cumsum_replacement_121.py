
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.full([1], 1)
        t2 = torch.cumsum(v1, 0).view([-1])
        return t2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
