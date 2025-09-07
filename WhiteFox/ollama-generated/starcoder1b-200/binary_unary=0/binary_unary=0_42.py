
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + other  # Apply pointwise convolution with kernel size 1 to the input tensor and add another tensor
        return torch.relu(v1)


# Initializing the model
m = Model(torch.randn(100, 3, 64, 64))
