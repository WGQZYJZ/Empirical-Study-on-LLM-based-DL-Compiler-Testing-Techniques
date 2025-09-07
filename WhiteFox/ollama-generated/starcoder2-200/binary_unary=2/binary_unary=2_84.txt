
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1): 
        v1 = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 - other_tensor # Subtract a tensor or scalar "other" from the output of the convolution
        v3 = torch.relu(v2) # Apply the ReLU (Rectified Linear Unit) activation function to the result

        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
