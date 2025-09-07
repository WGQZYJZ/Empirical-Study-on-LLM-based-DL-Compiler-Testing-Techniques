
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
       v0  = conv(x1) # Pointwise convolution with kernel size 1 to the input tensor 
       v1  = v0 + other # Add another tensor as the first argument of pointwise convolution 
       return torch.relu(v1)
 

# Initializing model