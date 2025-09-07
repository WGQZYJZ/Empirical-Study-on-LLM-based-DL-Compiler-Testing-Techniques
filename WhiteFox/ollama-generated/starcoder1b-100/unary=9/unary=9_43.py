
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + 3
        v2 = v1.clamp_(min=0).clamp_(max=6)
        v3 = (v4 / 6).round()
        return v3


# Initializing the model
m = Model()


