

class Model(torch.nn.Module):
    def __init__(self, m1):
        super().__init__()
        self.m1  = torch.nn.Conv2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply a convolution with kernel size 1 to the input tensor
        return [v1]

# Initializing the model