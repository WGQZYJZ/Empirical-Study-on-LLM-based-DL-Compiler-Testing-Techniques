
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=1, stride=1)
        self.pool1 = torch.nn.MaxPool2d(kernel_size=3, stride=3, padding=0)
        self.conv2 = torch.nn.Conv2d(36, 64, kernel_size=1, stride=1)
        self.pool2 = torch.nn.MaxPool2d(kernel_size=3, stride=3, padding=0)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v1 = self.pool1(v1)
        v2 = self.conv2(v1)
        v2 = self.pool2(v2)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
