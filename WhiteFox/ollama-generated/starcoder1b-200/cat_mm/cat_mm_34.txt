
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
 
    def forward(self, x1):
        # Convolve with another input tensor
        v1 = self.conv1(x1)
        # Concatenate the result along dimension 0
        v2 = torch.cat([v1, v1], dim=0)
        # Convolve with another input tensor
        v3 = self.conv2(v2)
        # Concatenate the result along dimension 1
        v4 = torch.cat([v3, v3], dim=1)
        return v4


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
