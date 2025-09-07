
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.convTranspose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.convTranspose(x1)
        v2 = (v1 > 0).float() # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        negative_slope  = torch.nn.LeakyReLU(negative_slope=negative_slope) # Initialize the negative slope parameter
        v3 = v2 * negative_slope # Multiply the output of the transposed convolution by a negative slope value
        v4 = torch.where(v2, v1, v3) # Apply the where function to select elements from t1 or t3 based on the mask t2
        return v4


# Initializing the model with negative slope 0.5