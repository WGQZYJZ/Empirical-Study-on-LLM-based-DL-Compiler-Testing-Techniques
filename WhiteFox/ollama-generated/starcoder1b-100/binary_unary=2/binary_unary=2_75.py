
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other):
        v1 = self.conv(x1) - other  # Subtract a tensor or scalar "other" from the output of the convolution
        v2 = torch.nn.functional.relu(v1)  # Apply the ReLU (Rectified Linear Unit) activation function to the result
        return v2


# Initializing the model
m = Model()


