
class Model(torch.nn.Module):
    def __init__(self, x1=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1) + x1 # Add another tensor to the output of the convolution
        return v1


# Inputs to the model
input_tensor = torch.randn(1, 3, 64, 64)
