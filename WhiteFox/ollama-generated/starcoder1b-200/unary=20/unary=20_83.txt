
class Upsample(nn.Module):
    def __init__(self, input_size=(128, 128)):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 32, 1, stride=1, padding=0)
        self.upsample = nn.Upsample(scale_factor=2, mode='nearest')
        self.relu = nn.ReLU()
 
    def forward(self, x):
        v1 = self.conv(x)
        v1 = self.upsample(v1)
        v2 = self.relu(v1)
        return v2


class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.upsample = Upsample((4, 4))
        self.conv = torch.nn.Conv2d(3, 32, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1 = self.conv(x)
        v1 = self.upsample(v1)
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()
