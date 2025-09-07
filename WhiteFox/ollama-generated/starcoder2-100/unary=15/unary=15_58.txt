
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply the pointwise convolution operation to an input tensor
        v2  = torch.nn.functional.relu(v1)# Apply the ReLU activation function to the output of the convolution
    return v2


# Initializing and running the model with different inputs