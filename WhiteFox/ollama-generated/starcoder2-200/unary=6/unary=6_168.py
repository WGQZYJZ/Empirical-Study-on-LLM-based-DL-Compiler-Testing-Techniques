
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 + 3 # Add 3 to the output of the convolution operation
        v3  = torch.clamp_min(v2, 0) # Clamp the result to a minimum of 0
        v4  = torch.clamp_max(v3, 6) # Clamp the previous output to a maximum of 6
        v5  = v1 * v4 # Multiply the output of the convolution by the clamped output 
        return v5 / 6


# Initializing the model and setting the input tensor
m = Model()
x1  = torch.randn(3, 8, 8)
 
# Forwarding the model through PyTorch
__output__   = m(x1)