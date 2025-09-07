
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bmm = torch.nn.Bmm2d()

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.bmm(v1, x2)
        return v2


# Inputs to the model
x1 = torch.randn(3, 4, 5)
x2 = torch.randn(3, 4, 6)
