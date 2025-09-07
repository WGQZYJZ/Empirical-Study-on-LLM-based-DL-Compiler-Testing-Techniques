
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        v = self.conv(x)
        # Apply the sigmoid function to the output of the transposed convolution
        t = sigmoid(v)
        # Multiply the output of the transposed convolution by the output of the sigmoid function
        y = x * t
        return y


# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
