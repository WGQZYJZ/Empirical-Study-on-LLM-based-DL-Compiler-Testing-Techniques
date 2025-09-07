
class ConvBNModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 16, kernel_size=3)
        self.bn   = torch.nn.BatchNorm2d(16)

    def forward(self, x):
        v1  = self.conv(x)
        v2  = self.bn(v1) # Batch normalization layer is not tracking running statistics 
        return v2

# Initializing the model
m = ConvBNModel()

 # Inputs to the model
x  = torch.randn(1,3,56,56)
__output__  = m(x)

