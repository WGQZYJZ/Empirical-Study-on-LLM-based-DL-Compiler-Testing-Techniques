
class Model(torch.nn.Module):
    def __init__(self, conv):
        super().__init__()
        self.conv = conv
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other
        return v2


# Initializing the model and setting the kernel size of convolution layer to 3.
conv_layer = torch.nn.Conv2d(3, 8, 3, stride=1, padding=0)
m = Model(conv_layer)
 
x1 = torch.randn(1, 3, 64, 64)
# Inputs to the model
