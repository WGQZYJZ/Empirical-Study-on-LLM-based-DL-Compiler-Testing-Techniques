
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor 
        v2  = v1 + v0   # Add another tensor `v0` to the output of the convolution
        return v2


# Initializing the model and setting the parameter of the addition operation
m  = Model()
m.conv[1] += m.conv[3].t().clone()
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

