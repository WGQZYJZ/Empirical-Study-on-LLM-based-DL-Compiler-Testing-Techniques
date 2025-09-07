
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.3):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 8, 1) # Pointwise transposed convolution
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3) # Apply the where function to select elements from v1 or v3 based on the mask v2
        return v4


# Initializing the model and setting the negative slope parameter
m  = Model(negative_slope=0.5)

# Inputs to the model
x1  = torch.randn(1,8,64,64)
__output__  = m(x1) # Evaluating the model