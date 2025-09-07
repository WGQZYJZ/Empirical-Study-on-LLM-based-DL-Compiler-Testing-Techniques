
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        v0  = x1 # Copy the input tensor (x1) to a new variable called v0
        v1  = self.conv(v0) # Apply pointwise convolution with kernel size 1 to the input of v0
        v2  = torch.nn.functional.relu(v1) # Apply ReLU activation function on the output of the convolution (v1) 
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

# Output from the model
__output__  = m(x1)

