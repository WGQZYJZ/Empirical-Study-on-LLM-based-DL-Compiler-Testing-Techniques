
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 16, stride=4, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.where(v1 > 0, v1 * -1, v1) # Apply Leaky ReLU to the output of the transposed convolution
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
