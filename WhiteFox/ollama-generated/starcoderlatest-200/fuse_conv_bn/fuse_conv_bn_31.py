
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @FuseConvBatchNorm
    def forward(self, x1):
        conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        bn = torch.nn.BatchNormXd(...)  # X should match with ConvXd
        output = bn(conv(input_tensor))
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
