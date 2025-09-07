
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5).type(torch.float)
        v3 = (v1 * 0.7071067811865476).type(torch.float)
        v4 = torch.erf((v3)).type(torch.float)
        v5 = (v2 * v4).type(torch.float)
        return v5


# Initializing the model
m = Model()


