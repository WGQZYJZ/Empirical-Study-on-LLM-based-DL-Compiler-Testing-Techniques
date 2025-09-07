
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) > 0
        v2 = (v1 * -1).log()
        v3 = v1 * (-2 + 3*v1 + 4*v1*v1)
        v4 = torch.where(v1, x1, v3)
        return v4


# Initializing the model
m = Model()


