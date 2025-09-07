
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=0)

    def forward(self, x):
        # Calculate the output of the first layer
        v1 = self.conv1(x)
        # Apply a pointwise convolution to the input tensor
        v2 = v1 * 0.5
        # Multiply the output of the convolution by 0.7071067811865476
        v3 = torch.nn.functional.hardshrink(v2)
        # Calculate the output of the second layer
        v4 = self.conv2(v3)
        # Add 1 to the output of the first and second layer
        v5 = v4 + 1
        # Multiply the output of the first and second layers by each other
        v6 = v5 * v1
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
