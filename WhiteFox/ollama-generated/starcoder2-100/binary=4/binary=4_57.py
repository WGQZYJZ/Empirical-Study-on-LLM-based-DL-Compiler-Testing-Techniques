
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.Linear(784, 20)(x1) # Apply linear transformation to the input tensor (assume that 784 is the total number of input pixels in MNIST dataset) 
        v2 = v1 + torch.zeros(v1.size()) # Add another zero tensor as a dummy input
        return v2


# Initializing the model
m = Model()
 

# Inputs to the model (a 784-dim vector, whose elements are in [0..1])
input_tensor = torch.rand(784) 
 
 
__output__  = m(input_tensor)
