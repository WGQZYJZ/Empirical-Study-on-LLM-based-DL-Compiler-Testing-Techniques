
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise transposed convolution to the input tensor
        v2  = v1  * 0.5      # Multiply the output of the transposed convolution by 0.5
        v3  = v1  * 0.7071067811865476    # Multiply the output of the transposed convolution by 0.7071067811865476
        v4  = torch.erf(v3)       # Apply the error function to the output of the transposed convolution
        v5  = v4 + 1            # Add 1 to the output of the error function
        v6  = v2 * v5         # Multiply the output of the transposed convolution by the output of the error function
        return v6


# Initializing the model
m = Model()

