
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = x1 + v2  # Add a tensor to the output of the convolution
        v3 = torch.relu(v2)  # Apply the ReLU activation function to the result
        return v3

# Initializing the model
m = Model()


