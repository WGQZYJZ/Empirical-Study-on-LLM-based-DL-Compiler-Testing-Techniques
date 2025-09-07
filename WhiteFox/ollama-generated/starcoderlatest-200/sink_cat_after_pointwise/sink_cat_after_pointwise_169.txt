
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, ..., xn):
        v = torch.cat([x1, x2, ..., xn], dim=0)
        return v


# Inputs to the model
x1 = torch.randn(5, 2, 2)
x2 = torch.randn(3, 2, 2)
