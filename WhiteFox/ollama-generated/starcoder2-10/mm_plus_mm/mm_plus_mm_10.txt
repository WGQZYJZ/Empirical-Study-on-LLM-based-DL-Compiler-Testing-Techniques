
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1  = torch.nn.Conv2d(3, 8, 7)
        self.m2  = torch.nn.MaxPool2d(kernel_size=4, stride=None, padding='same')
 
    def forward(self, x):
        v1  = self.m1(x) # Apply convolution with kernel size of 3*3 to the input tensor
        v2  = self.m2(v1) # Max pooling operation with the default window shape on the output of the convolution
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(5, 3, 64, 64)
__output__  = m(x)


