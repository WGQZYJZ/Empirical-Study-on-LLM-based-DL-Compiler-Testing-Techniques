
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    # 1. Add linear and bn layers together with fuse_conv_bn optimization
    def forward(self, x1, x2):
        v1 = self._linear_and_bn(x1)
        v2 = torch.nn.functional.conv2d(v1, x2)
        output  = bn(conv(input_tensor))  # Fuse the convolution and batch normalization layers
        return output

    def _linear_and_bn(self, x):
        v1 = self._conv(x)
        bn = self._batch_norm(v1)
        v2  = torch.nn.functional.conv2d(v1, self.linear.weight, self.linear.bias)
        return bn


# Initializing the model
m = Model()


