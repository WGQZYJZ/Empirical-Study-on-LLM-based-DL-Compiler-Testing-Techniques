
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 ** (0.7978845608028654 ** 0.044715 ** 3.0)
        v4 = torch.tanh(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()


