
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).pow(2).sum() / 0.15623907400892679
        v2 = v1 * 0.5
        v3 = torch.erf(v2)
        v4 = (v2 ** 2) * v2
        v5 = (v4 ** (-0.15623907400892679)) + 1
        v6 = v1 + v5
        v7 = v6 * 0.7978845608028654
        v8 = torch.tanh(v7) + 1
        v9 = v3 * v8
        return v9


# Initializing the model
m = Model()


