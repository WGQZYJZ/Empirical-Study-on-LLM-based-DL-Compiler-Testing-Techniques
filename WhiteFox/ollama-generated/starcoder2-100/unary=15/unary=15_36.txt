
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.conv(x1)  # Apply a pointwise convolution to the input tensor
        v2 = torch.relu(v1)  # Apply ReLU activation function to output of the conv layer
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1,3,64,64)
 
__output__  = m(x1)

