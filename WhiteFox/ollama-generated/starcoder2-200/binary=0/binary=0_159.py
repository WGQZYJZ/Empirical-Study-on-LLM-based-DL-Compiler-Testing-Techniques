
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + other  # Adding the "other" tensor to the output of the convolution
        return v2
        
m = Model(other="SomeOtherTensor")


# Initializing the model with "other" argument specified explicitly
m = Model(other=torch.randn(4, 8, 65, 65))
__output__  = m(x1)

# Initializing the model without any argument passed to it
m = Model()

