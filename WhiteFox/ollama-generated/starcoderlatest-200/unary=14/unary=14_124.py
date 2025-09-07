
class GLUNet(torch.nn.Module):
    def __init__(self, in_channel=3, out_channel=1, height=64, width=64):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channel, out_channel, 3, stride=1)
        # Add padding for convolution and transposed convolution
        self.conv_transpose = torch.nn.ConvTranspose2d(out_channel, in_channel, 3, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        v4 = self.conv_transpose(v3)
        return v4


# Initializing the model and input tensor to it
g_l_u_net = GLUNet()
x = torch.randn(1, 3, 64, 64)
