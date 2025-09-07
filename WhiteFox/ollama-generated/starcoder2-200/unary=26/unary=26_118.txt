
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.negative_slope = negative_slope
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise transposed convolution to the input tensor
        v2 = (v1 > 0).float() # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v3 = v1 * (-self.negative_slope) # Multiply the output of the transposed convolution by -negative slope
        v4  = torch.where(v2, v1, v3) # Apply the where function to select elements from v1 or v3 based on mask t2
        return v4
# Initializing the model with a negative slope parameter that is randomly initialized between `-0.5` and `0.5`. 
m = Model(torch.rand_like([0., -0.5]))

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
