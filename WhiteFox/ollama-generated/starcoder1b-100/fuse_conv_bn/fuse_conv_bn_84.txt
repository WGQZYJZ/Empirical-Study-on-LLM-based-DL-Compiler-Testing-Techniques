
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(...)
        self.batch_norm1 = torch.nn.BatchNormXd(...)

    def forward(self, x1):
        v1 = self.conv1(x1)  # X can be 1, 2, or 3 representing the dimension
        bn1 = self.batch_norm1(v1)  # Y should match with ConvXd
        output = bn1(v1)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
