
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.mm(x1, x2)
        return torch.cat([v, v, ...], dim=0)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 8, 64, 64)
x2 = torch.randn(2, 8, 64, 64)
