
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1,  other=None):
        v1  = self.conv(x1) 
        v2 = v1 + other if other is not None else v1 # add another tensor to the output of the convolution
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

# Setting other=None as a keyword argument
__output__  = m(x1) # The output of the model should be equal to v2 in the previous example

# Alternatively: setting another = None as an argument when calling `m`
__output__  = m(x1, other=None) # The output of the model should also be equal to v2 in the previous example.
