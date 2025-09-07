
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self, x):
        v1 = self.conv(x) # Apply a 2D convolution with kernel size of (1,1), stride of (1,1) and 1 padding to the input tensor
        v2 = torch.nn.functional.relu(v1) # Apply the ReLU activation function to the output of the convolution
        return v2

# Initializing the model
m = Model()
 
# Inputs to the model<|end_of_input|> 
x  = torch.randn(3, 8, 64, 64) # Generate a random input tensor with shape (number of channels, height, width)
__output__  = m(x)

