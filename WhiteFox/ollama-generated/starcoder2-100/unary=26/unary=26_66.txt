
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv = torch.nn.ConvTranspose1d(3, 8, 1)
    
    def forward(self, x1):
       v1 = self.conv(x1) # Apply pointwise transposed convolution to the input tensor
       v2 = v1 > 0 
       v4 = negative_slope * -v1 + torch.where(v2, v1, v3) # Multiply the output of the transposed convolution by the negative slope and apply where function
       return v4
# Initializing the model with negative slope=0.25:
m  = Model(negative_slope=0.25)

 # Inputs to the model
x1 = torch.randn(3, 64, 8)
