
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).square()
        v2 = v1 * 0.5
        v3 = v1.pow(2)
        v4 = v3.sqrt()
        v5 = v4.mul(v1)
        v6 = torch.tanh(v5) + 1
        v7 = v2.mul(v6)
        return v7


# Initializing the model
m = Model()


