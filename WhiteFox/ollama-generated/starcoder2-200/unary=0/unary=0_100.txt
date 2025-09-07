

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 + v2
        v4 = v3 + v2
        v5 = v4 + v2
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
