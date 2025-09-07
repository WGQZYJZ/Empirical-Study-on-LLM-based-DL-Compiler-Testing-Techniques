
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1 = self.conv(x).view(-1, 24, -1)
        return v1


# Inputs to the model
v1  = torch.randn(1, 3, 64, 64)
