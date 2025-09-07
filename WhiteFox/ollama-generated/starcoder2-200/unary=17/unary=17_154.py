
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1  = self.conv(x1) # Apply pointwise convolution to the input tensor
        t2  = torch.relu(t1) # Apply the ReLU activation function to the output of the convolution
        return t2

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(4, 8, 30, 30)


__output__  = m(x1)

