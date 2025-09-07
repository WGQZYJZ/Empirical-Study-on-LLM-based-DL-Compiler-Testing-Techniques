
class Model(torch.nn.Module):
    def __init__(self, conv_layer=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self.other_tensor # Add another tensor to the output of the convolution
        return v6


# Initializing the model
m = Model()
m.other_tensor = torch.randn(8, 8)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
