
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) - 0.5 # Subtract a scalar "0.5" from the output of the convolution
        v2 = torch.relu(v1) # Apply the ReLU (Rectified Linear Unit) activation function to the result
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
