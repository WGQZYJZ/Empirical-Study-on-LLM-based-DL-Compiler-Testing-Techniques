
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1): 
        v1 = self.conv(x1) # Applying pointwise convolution with kernel size 1 to the input tensor
        v2 = torch.tanh(v1)# applying hyperbolic tangent activation function to output of pointwise convolution
        return v2
        
# Initializing model
m = Model()

# Inputs to the model
x1 = torch.randn(1,3,64,64)
__output__  = m(x1)

