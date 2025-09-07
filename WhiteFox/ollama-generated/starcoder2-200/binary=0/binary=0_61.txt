
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1 + other


# Initializing the model
m = Model()
other = torch.randn(1, 32, 64, 64) # A dummy tensor used as another argument for adding to the output of a pointwise convolution in the forward function of our model
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
 
__output__, __other_outputs__  = m(x1), other

