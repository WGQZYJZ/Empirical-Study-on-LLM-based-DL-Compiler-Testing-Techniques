
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 > 0).to(dtype='bool') # the mask v2 contains True if each element in the output of the convolution is greater than zero, False otherwise
        v3 = torch.where(v2, v1, v1 * negative_slope) # where operator to select elements from the output of the convolution or multiplied by negative slope based on the mask v2 
        return v3

# Initializing the model and negative slope 
m = Model(-0.5) 

# Inputs to the model 
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

