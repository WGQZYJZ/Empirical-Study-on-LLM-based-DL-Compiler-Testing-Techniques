
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose1d(32, 64, 5) # Convolution with kernel size of 5, stride of 1 and a padding of 2 on the input tensor 
        self.neg_slope = negative_slope
 
    def forward(self, x):
        v1  = self.convT(x)
        v2  = v1 > 0 # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v3  = v1 * (-self.neg_slope)# Multiply the output of the transposed convolution by negative slope 
        v4  = torch.where(v2, v1, v3) # Apply where function to select elements from the input or the result based on mask
        return v4

# Initializing the model with negative slope
m  = Model(-0.5)

# Inputs for the model 
x1  = torch.randn(2, 32, 7) # Input to the model of shape 2 x 32 x 7 
 __output__  = m(x1)

