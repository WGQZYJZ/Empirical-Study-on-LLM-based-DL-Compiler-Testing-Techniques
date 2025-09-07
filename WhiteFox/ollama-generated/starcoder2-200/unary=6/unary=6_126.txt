
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv2d(x1) 
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0) # Clamps the output of the addition operation to a minimum value of 0
        v4  = torch.clamp_max(v3, 6) # Clamps the output of the clamping operation to a maximum value of 6 
        v5  = v1 * v4                  # Multiplies the output of the convolution by the clamped result
        v6  = v5 / 6                   # Divides the output of the multiplication by 6 
        return v6
 
# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)
