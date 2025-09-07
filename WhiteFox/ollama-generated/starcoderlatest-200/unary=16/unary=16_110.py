
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l = torch.nn.Linear(32 * 32 * 16, 50)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply a convolution with kernel size 7 to the input tensor
        v2 = relu(v1)       # Apply the ReLU activation function to the output of the convolution
        return linear(v2)   # Return the result of applying a linear transformation to the output of the convolution


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
