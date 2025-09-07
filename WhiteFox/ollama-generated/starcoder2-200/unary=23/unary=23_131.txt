
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = torch.tanh(x1) # Apply the hyperbolic tangent function to an input tensor. 
        return v2

 # Initializing the model
m = Model()
 
 # Input to the model
__input_1__ = torch.randn(4096, device=torch.device('cuda:0'))
 
# Obtaining output of the model for the input
__output__  = m(__input_1__)
 
