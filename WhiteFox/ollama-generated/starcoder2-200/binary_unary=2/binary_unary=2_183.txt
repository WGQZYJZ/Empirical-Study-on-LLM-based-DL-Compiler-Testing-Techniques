
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self, x): 
        v1  = self.conv(x) 
        v2  = v1 - other # Subtracting an input tensor or scalar value
        v4  = torch.relu(v2) # Apply the ReLU activation function to the result of the convolution
        return v4


# Initializing the model
m  = Model()
other = torch.zeros_like(x1)

# Inputs to the model
x1  = torch.randn(1,3,64,64)
__output__  = m(x1)

