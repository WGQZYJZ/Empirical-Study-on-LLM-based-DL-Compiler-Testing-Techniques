
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bmm = torch.nn.Bilinear(2, 2, 1)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 1, 2)
        v3 = torch.bmm(v1, v2)
        return self.bmm(v3, v3)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 2, 2)
x2 = torch.randn(2, 2, 2)
