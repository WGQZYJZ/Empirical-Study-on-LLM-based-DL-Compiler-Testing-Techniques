
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply a 1D convolution with kernel size 1 to the input tensor
        v2 = torch.clamp_min(v1, -3.) # Clamp the output of the convolution by subtracting 3 from each element
        v3 = torch.clamp_max(v2, +5.) # Subtract each element in the output of the previous operation by a constant and clamp to the minimum value
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
 x1  = torch.randn(1, 3, 64, 64)
 __output__  = m(x1)

