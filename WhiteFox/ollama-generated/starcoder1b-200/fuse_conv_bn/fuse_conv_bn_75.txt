
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1  = torch.nn.Conv2d(1, 2, kernel_size=(3, 3)) # X can be 1, 2, or 3 representing the dimension
        self.bn1 = torch.nn.BatchNorm2d(2)
        self.pool1 = torch.nn.MaxPool2d(kernel_size=2)

        self.conv2  = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn2 = torch.nn.BatchNormXd(...)  # X should match with ConvXd
        self.pool2 = torch.nn.MaxPoolNd(...)

        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1):
        v1 = self.pool1(torch.nn.functional.conv2d(x1, self.conv1.weight)) # X should be 'X * W'
        v1 = self.bn1(v1)

        v2 = self.pool2(self.conv2(self.pool1(v1))) # X can be 1, 2, or 3 representing the dimension
        v2 = torch.nn.functional.batch_norm(v2, affine=True)
        v2 = self.linear(v2)

        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 4, 5, 6)
