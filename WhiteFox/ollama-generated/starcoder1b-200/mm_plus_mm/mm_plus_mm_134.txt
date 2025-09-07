
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.MM

    def forward(self, x1, x2):
        v1 = self.mm(x1, x2)
        v2 = self.mm(x3, x4)
        return v3 + v5


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(2, 8, 64, 64)
