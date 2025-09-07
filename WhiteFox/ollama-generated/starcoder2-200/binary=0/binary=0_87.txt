
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other_tensor # A Tensor to be added to the output of the convolution operation in the model defined above.
        return v2


# Initializing the model with the passed tensor as keyword argument
other_tensor  = torch.randn(4, 5, 6)
m   = Model()
 

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

 __output__    = m(x1)

