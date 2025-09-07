
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x1):
        v1 = self.conv(x1) + 3 # Transposed convolution
        v2 = torch.clamp(v1, min=0) # Clamp the addition operation to a minimum of 0
        v3 = torch.clamp(v2, max=6) # Clamp the addition operation with a maximum of 6
        v4 = v1 * v3 # Multiply the transposed convolution by the clamp operation
        v5 = v4 / 6 # Divide the multiplication operation by 6 
        return v5

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 8, 32, 32)
