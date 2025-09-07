
class Model(torch.nn.Module):
    def __init__(self, conv_in_dim):
        super().__init__()
        self.conv = torch.nn.Conv2d(conv_in_dim, 64, 3)
        self.bn = torch.nn.BatchNorm2d(64)

    def forward(self, x1):
        x2 = F.relu(self.conv(x1))
        output = self.bn(x2)
        return output

# Inputs to the model
conv_in_dim = 3 # The dimension of the input tensor for convolution layer
x1 = torch.randn(1, conv_in_dim, 64, 64)
