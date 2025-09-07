
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x2):
        v2 = self.conv_transpose(x2)
        v2 *= 0.5
        v2 *= 0.7071067811865476
        v3 = torch.erf(v2)
        v4 = v3 + 1
        v5 = v2 * v4
        return v5


# Initializing the model
m = Model()


# Inputs to the model
x2 = torch.randn(8, 3, 64, 64)
