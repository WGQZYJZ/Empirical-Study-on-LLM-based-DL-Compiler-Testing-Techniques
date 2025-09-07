
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other # Subtract a tensor or scalar 'other' from the output of the convolution
        v3 = F.relu(v2) # Apply the ReLU (Rectified Linear Unit) activation function to the result
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

