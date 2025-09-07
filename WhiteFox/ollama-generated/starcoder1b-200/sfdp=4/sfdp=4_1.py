
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.pool  = torch.nn.MaxPool2d(kernel_size=2, stride=2)
 
    def forward(self, x):
        x  = self.conv1(x)
        x  = self.pool(x)
        return x


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 50, 70)
