
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.nn.functional.conv3d(...)(x1, x2)
        return self._fuse_conv_bn(v, 3) # X can be 1, 2, or 3 representing the dimension of inputs to the model

    def _fuse_conv_bn(self, v, ndim): 
        conv = torch.nn.functional.conv3d(...) # X should match with ConvXd
        bn  = torch.nn.functional.batch_norm(...)  # X should match with BatchNormXd
        return bn(conv(v))

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 2, 3, 3, 3)
x2 = torch.randn(1, 2, 3, 4, 5)
