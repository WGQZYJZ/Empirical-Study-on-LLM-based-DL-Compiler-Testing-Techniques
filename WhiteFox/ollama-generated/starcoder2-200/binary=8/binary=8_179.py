
class Model(torch.nn.Module):
    def __init__(self, someParam=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.param = someParam
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self.param # Add "someParam" to the output of the convolution operation. This is just an example and does not mean the model should contain this pattern.
        return v2


# Initializing the model with someParam set to 0
m = Model(3)


# Inputs to the model, and keyword argument value for the parameter "someParam" (this can be any number)
x1 = torch.randn(1, 3, 64, 64)
