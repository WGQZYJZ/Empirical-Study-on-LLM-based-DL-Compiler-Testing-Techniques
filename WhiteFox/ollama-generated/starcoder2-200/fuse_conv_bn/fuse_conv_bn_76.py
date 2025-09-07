
class Model(torch.nn.Module):
    def __init__(self, kernel_size=3):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 64, (kernel_size, kernel_size), bias=False)
        self.batchnorm = torch.nn.BatchNorm2d(64)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.batchnorm(v1)
        return v2

# Initializing the model with input size 3 by 50 by 84.
m = Model(kernel_size=3)

 # Inputs to the model. In this example, inputs have batch size of 2. 
x1 = torch.randn(2, 3, 50, 84).to(device='cuda')

__output__  = m(x1)

