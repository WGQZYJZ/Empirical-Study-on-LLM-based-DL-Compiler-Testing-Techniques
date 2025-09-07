
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        return torch.cat([x1, x2], dim=1)


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 4, 8, 8)
x2 = torch.randn(1, 5, 8, 8)
__output__  = m(x1, x2)


