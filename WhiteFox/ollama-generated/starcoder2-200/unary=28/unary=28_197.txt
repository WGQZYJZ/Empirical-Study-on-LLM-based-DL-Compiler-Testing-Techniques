
class Model(torch.nn.Module):
    def __init__(self, minv=0, maxv=-1):
        super().__init__()
        self.lin  = torch.nn.Linear(256 * 8, 4)
    
    def forward(self, x1):
        v1  = self.lin(x1) # Apply linear transformation to the input tensor
        v2  = torch.clamp_min(v1, minv) # Clamp the output of the linear transformation to a minimum value
        v3  = torch.clamp_max(v2, maxv) # Clamp the output of the previous operation to a maximum value
        return v3

# Initializing the model
minv  = -10.0 
maxv  =  5.0 

m  = Model(minv=minv, maxv=maxv)


# Inputs to the model
x2  = torch.randn(4, 256 * 8) # A random input of size (4, 192) is provided for testing purpose
__output__  = m(x2).sum()