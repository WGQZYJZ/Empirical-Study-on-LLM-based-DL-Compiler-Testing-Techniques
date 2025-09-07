
class Model(torch.nn.Module):
    def __init__(self, conv_dim):
        super().__init__()
        self.conv = torch.nn.ConvXd(2, 4, 3) if conv_dim == 1 else torch.nn.Conv2d(2, 8, 3) 
        # X can be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNormXd(...)

    def forward(self, x):
        output = self.conv(x)
        return self.bn(output)


# Initializing the model with conv_dim=2
m = Model(conv_dim=2)


# Inputs to the model
x  = torch.randn(1, 4, 2, 2)
