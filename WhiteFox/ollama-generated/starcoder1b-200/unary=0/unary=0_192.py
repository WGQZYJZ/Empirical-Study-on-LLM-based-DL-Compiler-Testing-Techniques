
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.square(v1)
        v3 = torch.pow(v2, 0.5)
        v4 = torch.pow(v3, 0.3333333333333333)
        v5 = torch.addcdiv(v4, v2, -1)
        v6 = torch.mul(x1, v5)
        return v6


# Initializing the model
m = Model()


