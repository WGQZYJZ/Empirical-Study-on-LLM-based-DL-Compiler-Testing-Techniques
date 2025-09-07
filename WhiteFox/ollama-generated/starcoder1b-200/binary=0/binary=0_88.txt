
class Model(torch.nn.Module):
    def __init__(self, other_tensor):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2=None):
        if x2 is not None:
            v1 = self.conv(x1, other_tensor)
        else:
            v1 = self.conv(x1)
        return v1


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.randn(1, 8, 64, 64)
