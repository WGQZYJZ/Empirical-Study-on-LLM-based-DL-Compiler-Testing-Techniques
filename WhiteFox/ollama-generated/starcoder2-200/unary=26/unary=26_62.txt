

class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 3)
 
    def forward(self, x1): 
        v1 = self.conv(x1) # Apply pointwise transposed convolution to the input tensor
        mask = v1 > 0  # Create a mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        negative_slope = -0.2 # Assigning a negative slope value as a constant for demonstration purposes. The negative slope should be user-defined by the user when using this example.
        v3 = torch.nn.LeakyReLU(negative_slope=negative_slope)(v1)  # Apply the Leaky ReLU to the output of the transposed convolution with the specified negative slope value (negative_slope).
        v4 = torch.where(mask, v1, v3) 
        return v4

# Initializing the model:
m  = Model()

