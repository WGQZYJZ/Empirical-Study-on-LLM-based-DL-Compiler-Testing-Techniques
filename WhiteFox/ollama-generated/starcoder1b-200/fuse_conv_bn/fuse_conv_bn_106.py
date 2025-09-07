
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(...)
        self.bn1  = torch.nn.BatchNormXd(...)
        self.pool1 = torch.nn.MaxPool2d(kernel_size=(2, 2))

    def forward(self, x1):
        v1 = self.pool1(self.bn1(self.conv1(x1)))
        # ... some additional operations ...
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 4, 3)
