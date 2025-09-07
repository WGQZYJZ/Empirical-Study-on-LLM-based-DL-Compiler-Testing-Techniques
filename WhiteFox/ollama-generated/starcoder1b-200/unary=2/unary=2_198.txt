
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = (torch.abs(v1) + 1) / 4
        v3 = (v1 + v2) * 0.7978845608028654
        v4 = torch.tanh(v3)
        v5 = v4 + 1
        v6 = (v2 * v5) + v3
        return v6


# Initializing the model
m = Model()


