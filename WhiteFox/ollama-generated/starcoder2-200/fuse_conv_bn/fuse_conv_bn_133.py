
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 5, kernel_size=3)
        self.conv2 = torch.nn.Conv2d(7, 8, kernel_size=(4, 3))
    def forward(self, x):
        output = conv1(x) # ConvXd is not in evaluation mode. BN is in evaluation mode tracking statistics. 
        output = torch.nn.functional.batchnorm2d(output)
        return output

m = Model()

