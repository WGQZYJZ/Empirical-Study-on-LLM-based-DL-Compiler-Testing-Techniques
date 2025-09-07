
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...) # X can be 1, 2, or 3 representing the dimension
        self.bn  = torch.nn.BatchNormXd(...) # X should match with ConvXd

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = self.conv(v1)  # Convolution operation is performed on the permuted tensor
        bn_output  = self.bn(v2)
        return bn_output


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
