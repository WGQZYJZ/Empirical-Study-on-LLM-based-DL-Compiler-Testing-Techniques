
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=3) # 3 channel input image 
        self.conv2 = torch.nn.Conv2d(3, 64, kernel_size=5) # 3 channel input image 
        self.bn = torch.nn.BatchNorm2d(8)

    def forward(self, x):
        v1  = torch.nn.functional.conv2d(x, self.conv1.weight, None, (1, 1), (0, 0)) # 3 channel input image 
        v2  = self.bn(torch.nn.functional.conv2d(v1, self.conv2.weight) + v1)
        return v2

# Initializing the model
m = Model()
# Inputs to the model
x_in = torch.randn(1000, 3, 80, 64) # The number of batch is fixed at 1000 here.


__output__  = m(x_in)


