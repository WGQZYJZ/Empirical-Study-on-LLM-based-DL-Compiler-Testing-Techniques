
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = t1 + t2
        return v3


# Inputs to the model
x1  = torch.randn(1, 5, 64, 64)
x2  = torch.randn(1, 8, 32, 32)
