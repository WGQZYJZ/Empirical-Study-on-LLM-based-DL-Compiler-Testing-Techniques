
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)

    def forward(self, x1):
        v0 = sigmoid(x1) # The initial activation is passed through the sigmoid function to produce a value between 0 and 1
        v1 = self.conv(v0) # Apply pointwise transposed convolution to this value
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
