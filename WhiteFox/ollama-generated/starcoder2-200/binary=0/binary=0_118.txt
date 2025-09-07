
class Model(torch.nn.Module):
    def __init__(self, x0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v4 = 5 + v1
        return v4


# Initializing the model