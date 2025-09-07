
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 2, kernel_size=3) # input channels x output channels x conv kernel_size[0] x conv kernel_size[1]
        self.bn1 = torch.nn.BatchNorm2d(2)  # input channel: number of feature maps, which equals to the number of classes in our dataset
    
    def forward(self, x):
        v1 = self.conv1(x)
        output = self.bn1(v1)
        return output

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 1, 20, 40)
