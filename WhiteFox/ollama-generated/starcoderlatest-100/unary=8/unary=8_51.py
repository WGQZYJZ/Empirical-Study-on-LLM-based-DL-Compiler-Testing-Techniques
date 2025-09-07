
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1) + 3 # Add 3 to the output of the transposed convolution
        v2 = torch.clamp(v1, min=0) # Clamp the output of the addition operation to a minimum of 0
        v3 = torch.clamp(v2, max=6) # Clamp the output of the previous clamp operation to a maximum of 6
        v4 = v1 * v3 # Multiply the output of the transposed convolution by the output of the clamp operation
        v5 = v4 / 6 # Divide the output of the multiplication operation by 6
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
