
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 3 to the input tensor 
        v2  = torch.relu(v1) + 10  # Add 10 to the ReLU activation function of the output of the pointwise convolution
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(3, 8, 56, 56)
