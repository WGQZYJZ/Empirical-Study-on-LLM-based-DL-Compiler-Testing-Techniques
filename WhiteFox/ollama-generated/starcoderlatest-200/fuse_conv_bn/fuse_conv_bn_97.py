
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)
        self.bn  = torch.nn.BatchNormXd(...)

    def forward(self, x1):
        output = self.conv(x1)
        # BatchNorm is a module, and the input tensor for BatchNorm has to be used in evaluation mode (not in training mode). 
        return self.bn(output)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
