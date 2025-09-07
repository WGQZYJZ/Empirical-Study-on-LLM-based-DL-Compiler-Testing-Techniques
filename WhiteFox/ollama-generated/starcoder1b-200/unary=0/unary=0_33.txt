
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).pow(2)
        v2 = v1 * 0.5
        v3 = v1 * (v1 * 1 / 3).sqrt()
        v4 = v3 * (v1 * -1 / 9).sqrt()
        v5 = v4 * 4 * 3 / (1 + torch.tanh(v7))
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()

