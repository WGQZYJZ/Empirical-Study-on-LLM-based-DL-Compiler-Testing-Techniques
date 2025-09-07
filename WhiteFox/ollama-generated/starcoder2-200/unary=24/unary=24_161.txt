

class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.156249978304)
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2  = (v1 >0).float() # create a boolean mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise 
        v3  = v1 * negative_slope   # multiply the output of the convolution by the negative slope 
        v4  = torch.where(v2, v1, v3)    # apply the where function to select elements from v1 or v3 based on the mask v2
        return v4

# Initializing the model with a custom negative slope
negative_slope  = 0.156249978304
m  = Model(negative_slope)

# Inputs to the model
x1   = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

