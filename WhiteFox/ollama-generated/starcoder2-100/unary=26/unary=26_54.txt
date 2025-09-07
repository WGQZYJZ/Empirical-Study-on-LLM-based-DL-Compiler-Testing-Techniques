
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.deconv(x1)
        v2  = (v1 > 0).float() # Create a mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        v3  = v1 * negative_slope  # Multiply the output of the transposed convolution by the negative slope 
        v4  = torch.where(v2, v1, v3) # Apply the where function to select elements from v1 or v3 based on the mask v2
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
