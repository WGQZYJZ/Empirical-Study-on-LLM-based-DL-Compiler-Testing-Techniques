
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1): 
        v1  = self.conv(x1)
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0) # Add 3 to the output of the transposed convolution
        v4  = torch.clamp_max(v3, 6) # Clamp at a minimum value of 0 and maximum value of 6 for the previous output 
        v5  = v4 / 6   # Divide by 6 on the previous output
        return v5


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 28, 28)
__output__  = m(x1)

