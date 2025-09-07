
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1  = self.conv(x1)
        mask  = (v1 > 0).float() # Create a mask where each element is True if the corresponding element in v1 is greater than 0 and False otherwise 
        v2  = v1 * -self.negative_slope # Multiply the output of the transposed convolution by the negative slope 
        v3  = torch.where(mask, v1, v2) # Apply the where function to select elements from v1 or v2 based on the mask 
        return v3

# Initializing the model with negative slope=0.25
negative_slope  = 0.25
m  = Model(negative_slope)


# Inputs to the model 
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)
