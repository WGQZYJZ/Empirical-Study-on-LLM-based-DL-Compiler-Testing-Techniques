
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        v = torch.full([4], 3, dtype=torch.long)
        t = v * v
        return torch.abs(t + 1)


# Inputs to the model
x1 = torch.randn(2, 2)
