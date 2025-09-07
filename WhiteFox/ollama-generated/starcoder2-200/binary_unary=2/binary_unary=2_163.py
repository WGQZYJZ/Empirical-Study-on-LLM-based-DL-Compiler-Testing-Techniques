
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        v1  = self.conv(x1)

        # Subtracting a scalar from the output of the convolution
        v4  = v1 - 0.5

        # Apply ReLU activation function to the result
        v2  = torch.nn.functional.relu(v4)
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

