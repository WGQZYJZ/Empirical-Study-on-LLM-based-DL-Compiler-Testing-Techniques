
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 16, stride=2, padding=0)
        self.leaky_relu = torch.nn.LeakyReLU()
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1) > 0 # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 * negative_slope # Multiply the output of the transposed convolution by the negative slope
        return torch.where(v1, v2, x1)


# Initializing the model
m = Model()

