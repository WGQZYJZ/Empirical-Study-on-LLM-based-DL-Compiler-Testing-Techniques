
class Model(torch.nn.Module):
    def __init__(self, conv_ndims=1):
        super().__init__()
        # input tensor
        self.conv = torch.nn.ConvXd(2, 2)
        # output tensor
        self.bn  = torch.nn.BatchNormXd(2)

    def forward(self, x1):
        if self.training:
            x1 = self.conv(x1)  # use convX to make a trainable model 
            x1 = self.bn(x1)   # Use BN as normal operator
        else:
            # Use convX to make a frozen inference model 
            x1 = self.conv(x1)
            x1 = self.bn(x1)
        return x1


# Inputs to the model
x1 = torch.randn(1, 2, 3, 3)
