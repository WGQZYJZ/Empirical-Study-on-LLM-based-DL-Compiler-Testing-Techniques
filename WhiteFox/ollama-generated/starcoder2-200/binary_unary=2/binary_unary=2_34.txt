
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v0 = x1
        v1  = self.conv(v0) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 - other
        v3  = torch.relu(v2) # Apply the ReLU (Rectified Linear Unit) activation function to the result of subtraction
        return v3

# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
other  = torch.randn(8, 8, 5, 5) # other is a random tensor with shape (channels=8, kernel_size=(5 x 5))

__output__  = m(x1)

