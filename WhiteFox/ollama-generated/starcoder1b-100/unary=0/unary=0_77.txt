
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).pow(2)
        v2 = (v1 * 0.5).sqrt()
        v3 = (v1 * v1).pow(2).sqrt()
        v4 = (v3 * v1).mul_(0.044715)
        v5 = v1 + v4
        v6 = v5.mul_(0.7978845608028654)
        return v6


# Initializing the model
m = Model()


