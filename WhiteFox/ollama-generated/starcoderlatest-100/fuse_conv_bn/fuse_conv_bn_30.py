
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)
        self.bn = torch.nn.BatchNormXd(...)

    def forward(self, x):
        output  = self.conv(x)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 2, 2, 2)
