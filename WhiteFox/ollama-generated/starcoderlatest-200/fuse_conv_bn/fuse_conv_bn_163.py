 2
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(2, 20, kernel_size=(5, 5))
        self.batchnorm1 = torch.nn.BatchNorm2d(20)

    def forward(self, x1):
        # The first conv and batch norm layer are in evaluation mode, so we fuse them into a single convolution layer with BatchNorm2d
        x2 = self.conv1(x1) 
        x3 = self.batchnorm1(x2)
        return x3


# Initializing the model 2
m = Model() 

# Inputs to the model 2
x1 = torch.randn(1, 2, 60, 80)
