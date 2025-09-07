
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)

    def forward(self, x1):
        v1  = self.conv(x1) + 3
        v2  = F.clamp(v1, min=0) # Apply the clamp operation to the output of the addition operator
        v3  = torch.clamp(v2, max=6) # Clamp the output of the previous clamp operator
        v4  = v1 * v3  # Multiply the output of the transposed convolution by the clamped output 
        v5  = v4 / 6  # Divide the output of the multiplication operation by 6
        return v5

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
