
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        l1 = self.conv(x1)
        l2 = clamp(min=0, max=6, l1 + 3) / 6
        return l2


# Initializing the model
m = Model()


