
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x):
        v1  = self.conv(x[:, :9223372036854775807])
        v2  = torch.cat([v1, x[:size]], dim=1)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x = torch.randn(3, 64, 64)
