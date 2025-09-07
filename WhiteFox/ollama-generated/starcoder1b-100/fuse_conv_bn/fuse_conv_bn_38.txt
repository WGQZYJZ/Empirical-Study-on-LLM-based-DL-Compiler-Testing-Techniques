
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    @staticmethod
    def _fuse_conv_bn(conv, bn):
        conv = conv[..., None]
        bn = bn[..., None]

        return torch.nn.functional.conv3d(conv, bn, stride=1), torch.nn.functional.batch_norm3d(bn, eps=1e-5)

    @torch.jit.export
    def forward(self, x1):
        return Model._fuse_conv_bn(*self._fuse_conv_bn(x1, self.linear.weight))(x1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2, 3)
