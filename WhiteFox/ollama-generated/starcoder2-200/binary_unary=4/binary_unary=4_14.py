
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=None):
        v0  = torch.randn(256, 3) # Random initialization of an input tensor 
        v1  = self._linear(v0).reshape((8, -1)) # Linear transformation on the input tensor
        v4  = torch.relu(other + v1) # ReLU activation function is applied to another tensor added to the output of the linear transformation
        return v4
 

# Initializing the model
m = Model()
 
# Inputs to the model
x2 = torch.randn(3, 56, 57) 
__output__  = m(x1, other=x2)

