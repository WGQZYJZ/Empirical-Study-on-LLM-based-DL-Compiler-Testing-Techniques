
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 ** 0.5).sqrt()
        v3 = (v1 ** 2.0).pow_(0.5)
        v4 = ((v3 * v3) ** 0.5).sqrt_()
        v5 = ((v4 * v1) ** 0.5) + 1
        v6 = (v2 * v9)
        return v6


# Initializing the model
m = Model()

