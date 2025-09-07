
class Model(torch.nn.Module):
    def __init__(self, conv, bn):
        super().__init__()

        self.conv = conv
        self.bn = bn

    def forward(self, x1):

        # Fuse the ConvXd and BatchNormXd layers into a single ConvXd layer using torch.nn.fuse_conv_bn() function
        output = torch.nn.fuser_conv_bn()(x1)  # Use fused_conv_bn to fuse the conv and bn layers together

        return output

# Inputs to the model