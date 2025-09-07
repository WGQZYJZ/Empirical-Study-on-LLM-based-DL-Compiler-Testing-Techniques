
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 + torch.randn_like(v1)*5 # Add a random number between -5 and +5 to the output of the convolution
        v3  = torch.relu6(v2) # Apply ReLU function to the output of the convolution
        v4  = v3 *0.7071067811865476 # Multiply the output of the ReLU by a constant value
        return v4

# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)