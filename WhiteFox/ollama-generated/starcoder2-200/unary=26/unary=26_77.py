
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3,8,1) # Create a transposed convolution with kernel size 1
        self.leakyrelu = torch.nn.LeakyReLU(negative_slope)  # Create a LeakyReLU layer
 
    def forward(self, x):
        v1 = self.conv(x) 
        v2 = (v1 > 0).float() # Create a mask where each element is True if the corresponding element in t1 is greater than 0 and False otherwise
        v3 = v1 * -0.5 # Multiply the output of the transposed convolution by negative_slope
        v4 = torch.where(v2,v1,v3) # Apply the where function to select elements from the output of the transposed convolution or the result of multiplication based on the mask
        return self.leakyrelu(v4)


# Initializing the model with negative slope 0.5