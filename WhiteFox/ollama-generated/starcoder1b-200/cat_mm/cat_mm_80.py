
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        v1 = torch.mm(x1, x1)
        v2 = v1 + 0.5
        v3 = v2 * 2.718281828459045
        return v3


# Initializing the model
m = Model()


