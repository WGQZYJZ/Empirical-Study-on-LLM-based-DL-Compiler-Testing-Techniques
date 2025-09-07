
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = (v1 ** 2).sqrt()
        v3 = (v1 ** 4) / 27.976
        v4 = torch.tanh(v3) + 1
        v5 = v2 * v4
        v6 = v5 * 0.7978845608028654
        return v6


# Initializing the model
m = Model()


