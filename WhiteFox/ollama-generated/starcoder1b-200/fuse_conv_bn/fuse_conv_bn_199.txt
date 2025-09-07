
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNormXd(...) # X should match with ConvXd

    @torch.jit.export
    def forward(self, x1):
        conv_result = self.conv(x1) # Fuse the convolution layer and batch normalization layer
        bn_output = self.bn(conv_result)   # Batch normalization layer is fused to conv

        return bn_output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
