
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply pointwise transposed convolution to the input tensor 
        v2 = (v1 > 0).to(torch.float32) # Create a mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        v3 = v1 * negative_slope # Multiply the output of the transposed convolution by the negative slope 
        v4 = torch.where(v2 == 1., v1, v3) # Apply the where function to select elements from v1 or v3 based on the mask v2
        return v4


# Initializing the model
negative_slope=0.5
m = Model(negative_slope=negative_slope)


