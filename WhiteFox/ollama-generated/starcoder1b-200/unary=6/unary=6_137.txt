
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 + 3).clamp_(0, 6)
        v3 = (v2 - 6).clamp_(-3, 4)
        v4 = v1 * v3
        return v4


# Initializing the model
m = Model()


