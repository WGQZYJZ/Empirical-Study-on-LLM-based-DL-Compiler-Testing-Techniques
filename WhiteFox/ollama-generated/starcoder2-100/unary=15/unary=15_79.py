
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.relu  = torch.nn.ReLU()
 
    def forward(self, x):
        v1  = self.conv(x) # Pointwise convolution with kernel size of 1 on the input tensor
        v2  = self.relu(v1) # Apply ReLU activation to output of pointwise convolution operation
        return v2


m = Model()

# Inputs for the model
x  = torch.randn(1,3,64,64)
__output__  = m(x)