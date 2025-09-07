
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Pointwise convolution with kernel size of 1
        v2  = v1 + torch.randn_like(v1) # Add another tensor to the output of the pointwise convolution 
        v3  = torch.relu(v2) # Apply the ReLU activation function to the result
        return v3

# Initializing model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

