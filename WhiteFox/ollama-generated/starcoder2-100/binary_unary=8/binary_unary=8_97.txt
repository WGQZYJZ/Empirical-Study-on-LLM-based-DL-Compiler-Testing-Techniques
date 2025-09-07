
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 + torch.randn(v1.size()) * 345 
        v3  = F.relu(v2) # Apply the ReLU activation function to the result 
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

__output__= m(x1)
