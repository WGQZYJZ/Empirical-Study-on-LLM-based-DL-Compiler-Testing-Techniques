
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv_transpose(x1) # Apply pointwise transposed convolution to the input tensor
        v2  = v1 + 3 
        v3  = torch.clamp(v2, min=0) # Clamp the output of the addition operation to a minimum of 0
        v4  = torch.clamp(v3, max=6) # Clamp the output of the previous clamp operation to a maximum of 6
        v5  = v1 * v4 
        v6  = v5 / 6 
        return v6


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1,3,80,79)
 
