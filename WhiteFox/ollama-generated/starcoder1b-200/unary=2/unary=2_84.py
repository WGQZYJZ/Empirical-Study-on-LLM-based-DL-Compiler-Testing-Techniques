
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=1)
 
    def forward(self, x2):
        v2 = self.conv(x2) * 0.5
        v3 = v2 ** 3
        v4 = v2 + v3
        v5 = torch.tanh(v4)
        v6 = v5 + 1
        v7 = v2 * v6
        return v7


# Initializing the model
m = Model()


# Inputs to the model
x2 = torch.randn(3, 8, 64, 64)
