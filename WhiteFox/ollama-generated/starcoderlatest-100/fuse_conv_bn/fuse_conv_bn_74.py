
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(...)
        self.bn1   = torch.nn.BatchNormXd(...)

    def forward(self, x1):
        v1  = conv_module.foward(x1)    # `forward` of the module object
        bn  = batch_norm_module.forward(v1)    # `forward` of the module object
        output = self.bn2(self.conv3d(bn))   # Use convXd's functional equivalent

        return output

# Initializing the model
m = Model()
input_tensor  = torch.randn(1, 10, 4096)
