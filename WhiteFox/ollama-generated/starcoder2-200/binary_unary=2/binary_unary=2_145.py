
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other 
        v3  = torch.relu(v2) # Apply the ReLU activation function to the output of the pointwise convolution minus a tensor or scalar
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
other = torch.randn(8).to(dtype=torch.float32)
__output__  = m(x1)

