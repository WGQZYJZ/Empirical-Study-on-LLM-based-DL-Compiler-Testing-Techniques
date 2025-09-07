
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.cat  = torch.nn.Cat()
 
    def forward(self, x1): 
        v0  = self.conv(x1) # Convolve the input tensor with a kernel size of 1
        v1  = torch.addmm(v0, mat1, mat2) # Add two matrices together and then convolve it again using a kernel size of 1
        v2  = self.cat([v1], dim) 
        return v2
 

# Initializing the model with input dimension as zero
m_dimzero  = Model(0)
__output__  = m_dimzero(x1)


# Initializing the model with input dimension set to 0 by default, and setting it to -3 when calling. The model is initialized in the forward method using a constant tensor as an input argument
m  = Model(-3)  # Initialize the input dimension using a constant value of -3.
__output__  = m(x1)

