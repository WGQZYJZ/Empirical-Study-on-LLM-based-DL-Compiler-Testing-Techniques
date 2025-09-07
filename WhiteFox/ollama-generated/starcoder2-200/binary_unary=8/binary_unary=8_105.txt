
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v4  = v1 + t0  # Add a tensor to the output of the convolution 
        v5  = torch.relu(v4) # Apply the ReLU activation function to the result
        return v6

# Initializing the model
m = Model()


# Inputs to the model