
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.pool  = torch.nn.MaxPool2d(kernel_size=2, stride=None, padding=0, ceil_mode=False)
 
    def forward(self, x):
        v1 = self.conv(x)
        v3  = v1 * 0.7853981633974483 #Multiply the output of the convolution by 0.7853981633974483
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(2, 3, 16, 16)

__output__  = m(x)
