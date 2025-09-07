
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.conv1(x) * 0.5
        v2 = self.conv2(v1).transpose(-2, -1)  # Transpose the input tensor to match the output shape of conv2
        # Scale the dot product by an inverse scale factor
        # Apply softmax to the scaled dot product
        # Apply dropout to the softmax output
        return v2

# Initializing the model
m = Model()


