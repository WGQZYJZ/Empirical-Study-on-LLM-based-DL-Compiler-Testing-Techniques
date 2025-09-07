
class Model(torch.nn.Module):
    def __init__(self, other_tensor):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, y2):
        v1 = self.conv(x1)
        v2 = (y2 + other_tensor)
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
y2 = torch.randn(1, 3, 64, 64)
