
class Model(torch.nn.Module):
    def __init__(self, n_channels=32):
        super().__init__()
        self.conv1  = torch.nn.Conv2d(n_channels, 8, 3)
        self.conv2  = torch.nn.Conv2d(8, 64, 3)

    def forward(self, x0):

        out = self.conv1(x0) # Apply pointwise convolution with kernel size 3 to the input tensor
        out = self.conv2(out) # Apply pointwise convolution with kernel size 3 to the output of the previous convolution
        v1  = torch.cat([torch.ones_like(t1), t1, ..., t1])# Concatenation of three copies of a tensor

        return out + v1


# Initializing and generating the model example