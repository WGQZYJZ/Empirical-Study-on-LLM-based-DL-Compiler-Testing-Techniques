
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - 0.5 # Subtract the value of "other" from the output of the convolution
        v3  = torch.nn.functional.relu(v2)  # Apply the ReLU (Rectified Linear Unit) activation function to the result
        return v3


# Initializing the model and inputs