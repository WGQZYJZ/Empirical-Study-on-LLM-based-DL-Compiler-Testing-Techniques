
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x1):
        v0  = relu(v5) # Apply the ReLU activation function to the output of the transposed convolution
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 8, 32, 32)
