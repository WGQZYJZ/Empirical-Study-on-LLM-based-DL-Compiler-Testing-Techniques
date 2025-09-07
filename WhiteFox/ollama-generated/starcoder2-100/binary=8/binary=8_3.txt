
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 + self._add_other(v1) # Add another tensor to the output of the convolution
 
        return v2
 
    def _add_other(self, v): 
        return torch.randn(8, 5, 43, 67)


# Initializing the model
m = Model()

# Inputs to the model 
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)
