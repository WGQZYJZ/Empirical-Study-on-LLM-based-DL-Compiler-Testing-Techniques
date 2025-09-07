
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.conv(x1)  # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 + torch.zeros([v1], dtype=torch.float32)  # Add another tensor to the output of the convolution
        v3 = torch.relu(v2)  # Apply the ReLU activation function to the result 
        return v3


# Initializing and running the model