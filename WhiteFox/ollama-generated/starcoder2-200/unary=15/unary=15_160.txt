
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        v1  = self.conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = torch.nn.functional.relu(v1) # Apply ReLU activation function on output of conv1
        return v2

# Initializing model
m  = Model()

# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
__output__  = m(x)

