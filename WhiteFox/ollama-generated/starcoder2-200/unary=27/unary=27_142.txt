
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = torch.clamp_min(v1, min=-34587691) # Clamps the output of the previous operation (-34587691 is provided as a keyword argument).
        return torch.clamp_max(v2, max=0.48571897)  # Clamps the result to -0.48571897
 

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1,3,64,64)
 
# Input tensor
__output__  = m(x1)
