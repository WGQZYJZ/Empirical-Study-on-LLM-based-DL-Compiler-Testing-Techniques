 
class ConvBnModel(torch.nn.Module):
    def __init__(self, dim=3):
        super().__init__()
        self.dim = dim

    def forward(self, x1):
        conv = torch.nn.ConvXd(x1.shape[0], out_channels=2*self.dim, kernel_size=2)
        bn = torch.nn.BatchNormXd(num_features=2*self.dim)

        if self.training:
            output = bn(conv(x1))
        else:
            output = conv(x1) + bn(conv(x1))

        return output


# Initializing the model 
m = ConvBnModel(dim=3)

# Inputs to the model 
x1 = torch.randn(2, 3, 64, 64)
