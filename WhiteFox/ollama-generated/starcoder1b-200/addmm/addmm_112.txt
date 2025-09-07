
class Model(torch.nn.Module):
    def __init__(self, inp=0.5):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, inp=1):
        v1 = self.conv(x1)
        v2 = v1 + inp
        return v2


# Initializing the model
m = Model()


