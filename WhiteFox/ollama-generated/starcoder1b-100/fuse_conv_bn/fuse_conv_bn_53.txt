
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @staticmethod
    def fuse_conv_bn(conv, bn):
        # The input tensors need not be compatible. 
        conv = conv(conv)  # Use conv() as the input for the batch normalization layer
        bn   = bn(bn)

        return torch.nn.functional.conv2d(input=conv, output=bn)

    def forward(self, x1):
        # Fuse the convolution and the batch normalization layer together.
        conv  = torch.nn.functional.conv2d(input=x1, ...).view(...)
        bn    = torch.nn.functional.batch_norm(...).view(...)
        return self.fuse_conv_bn(conv, bn)


# Inputs to the model
x1 = torch.randn(1, 2, 32, 32)
