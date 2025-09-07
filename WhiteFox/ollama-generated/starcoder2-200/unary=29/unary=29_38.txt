
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v0 = torch.randn(1, 4, 64, 64) # Create a new input tensor with the shape (batch_size, channels, width, height). Use torch.randn to create the new input tensor.
        v1  = self.convT(v0) # Apply a pointwise transposed convolution on the created random input.
        v2 = torch.clamp(v1, min=3.0) # Clamps the output of v1 to minimum value (3 in this case).
        v3 = torch.clamp_max(v2, max=5.0)# Clamps the output of previous operation to a maximum value (5 in this case.)
        return v3

# Initializing and running the model