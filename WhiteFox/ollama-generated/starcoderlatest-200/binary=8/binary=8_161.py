
class Model(torch.nn.Module):
    def __init__(self, conv2d=True):
        super().__init__()
        if conv2d:
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other=None):
        if conv2d:
            v1 = self.conv(x1)
            return v1 + other
        else:
            return None
 

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.tensor([0.5])
