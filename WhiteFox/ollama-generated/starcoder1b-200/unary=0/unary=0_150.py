
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = v1 ** 2
        v3 = v2 * v1
        v4 = torch.tanh(v3)
        v5 = v4 + 1
        v6 = v1 * v9
        return v6


# Initializing the model
m = Model()


