
class Model(torch.nn.Module):
    def __init__(self, negative_slope = 0.5):
        super().__init__()
        self.convTranspose  = torch.nn.ConvTranspose2d(3, 8, 1) # Define the pointwise transposed convolution layer
        self.leakyReLU = torch.nn.LeakyReLU(negative_slope= negative_slope)
 
    def forward(self, x):
        v0  = self.convTranspose (x) # Apply the pointwise transposed convolution to the input tensor
        mask = v0 > 0 # Create a mask where each element is True if the corresponding element in v0 is greater than 0, False otherwise 
        v1  = v0 * (-2.0) # Multiply the output of the transposed convolution by -2.0
        v2  = torch.where(mask,v0,-v1) # Apply the where function to select elements from v0 or the result of the multiplication based on the mask
        return self.leakyReLU (v2 )


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(1,3,64,64) # Generating a random tensor as an input for the model 

# The output of the model

