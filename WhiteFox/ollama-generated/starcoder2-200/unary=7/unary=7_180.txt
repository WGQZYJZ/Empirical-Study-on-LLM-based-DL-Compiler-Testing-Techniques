
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = l * clamp(min=0, max=6, l1 + 3)
        v3  = v2 / 4
        return v3

# Initializing the model
m = Model()

