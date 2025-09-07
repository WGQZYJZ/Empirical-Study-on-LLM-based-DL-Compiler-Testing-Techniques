
class Model(torch.nn.Module):
    def __init__(self, min_value=-0.5, max_value=1.5):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - min_value
        v3 = max_value - v2
        return v3


# Initializing the model
m = Model(-0.5, 1.5)

