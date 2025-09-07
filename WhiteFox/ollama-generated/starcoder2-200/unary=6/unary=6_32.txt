
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 + 3        # add 3 to the output of the convolution 
        v3  = torch.clamp_min(v2,0)# clamp the output of the addition operation to a minimum of 0
        v4  = torch.clamp_max(v3,6)    # clamp the output of the previous operation to a maximum of 6
        v5  = v1 * v4       # multiply the output of the convolution by the clamped result 
        v6  = v5 / 6        # divide the output of the multiplication operation by 6
        return v6
 

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(2,3, 720, 1280)
