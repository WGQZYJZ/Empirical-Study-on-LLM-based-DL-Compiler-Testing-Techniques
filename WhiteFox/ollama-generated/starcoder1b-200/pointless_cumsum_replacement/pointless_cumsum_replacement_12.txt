
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).permute((2, 0, 1)) # Make the first two dimensions of input tensor equal to output
        return torch.cumsum(v1, 1).permute((1, 2, 0))


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
