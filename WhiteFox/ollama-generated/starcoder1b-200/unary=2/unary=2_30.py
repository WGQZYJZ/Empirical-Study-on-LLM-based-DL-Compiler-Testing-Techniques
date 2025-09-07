
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = torch.pow(v1, 1.5)
        v4 = torch.erf(v3)
        v5 = torch.mul(v4, -0.7978845608028654)
        v6 = torch.tanh(v5)
        v7 = torch.add(torch.mul(v1, 0.7071067811865476), v4)
        return v7


# Initializing the model
m = Model()


