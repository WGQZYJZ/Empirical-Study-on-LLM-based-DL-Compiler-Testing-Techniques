
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv(x1, x2) + 0.5  # Add a constant to the result of the convolution
        v2 = torch.relu(v1)  # Apply ReLU activation function to the output of the convolution
        return v2


# Initializing the model
m = Model()

