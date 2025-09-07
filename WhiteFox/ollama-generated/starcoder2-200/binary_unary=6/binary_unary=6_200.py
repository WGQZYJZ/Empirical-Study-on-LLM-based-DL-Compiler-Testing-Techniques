
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
 
        v0 = self.conv(x1)  # Apply a pointwise convolution to an input tensor
        v1 = torch.relu(v0)  # Apply the ReLU activation function to 'v0'

        return 3


# Initializing model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 8, 64, 64)

__output__  = m(x1)
