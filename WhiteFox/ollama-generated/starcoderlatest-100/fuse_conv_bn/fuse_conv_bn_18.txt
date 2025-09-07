 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 64, kernel_size=5)
        self.batchnorm = torch.nn.BatchNorm2d(64)

    def forward(self, x1):
        output = self.conv(x1).permute(0,3,1,2).contiguous()
        output = self.batchnorm(output) # Use the conv layer as an input for batch norm
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 32, 32)
