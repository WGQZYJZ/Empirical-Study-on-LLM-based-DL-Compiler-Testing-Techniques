
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self,x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 + other 
        v3  = torch.relu(v2) # Apply the ReLU activation function to the result
        return v3

# Initializing model