
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (v1 > 0).float() # Boolean mask
        slope = -negative_slope * mask + mask 
        v2 = torch.where(mask, v1, slope) # Where function to multiply the output of the convolution by a negative slope if the element in t2 is True or the output of the convolution otherwise.
        return v2


# Initializing the model and setting the negative_slope parameter
m = Model(negative_slope=0.5)
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # Input tensor
