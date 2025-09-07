
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)

    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if other is not None:
            v2 = v1 - other

        return v2

m = Model()

# Inputs to the model
x1  = torch.randn(10, 3)
__other__ = torch.zeros((10, 4))

