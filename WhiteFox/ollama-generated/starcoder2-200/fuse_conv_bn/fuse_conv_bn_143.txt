
class FusedConvBnModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvXd(in_channels=2, out_channels=4) # X is one of the following values: 1, 2 or 3
        self.bn   = torch.nn.BatchNormXd(num_features=4)

    def forward(self, input):
        return self.bn(torch.nn.functional.convXd(input, self.conv))


# Initializing the model
m  = FusedConvBnModel()

# Input to the model: 1 X 2 3-dimensional tensor
x_fused   = torch.randn(256, 4) # Assuming X is one of 1, 2 or 3
