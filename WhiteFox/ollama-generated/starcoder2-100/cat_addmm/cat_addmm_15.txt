
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1):
        v2  = torch.cat([x1], dim=0) 
        return v2


# Initializing the model with a specific dimensionality (dimension must be 4). This is used to ensure that the concatenation operation is performed along the `dim` of the input tensor and not an arbitrary dimension number
m = Model(3)

 # Inputs to the model. Here, the input size is [8, 2] for the first input and a shape similarly varying second input
x1  = torch.randn(4, 56).reshape([7, 2]) # First input to the model of size [7, 2]

 __output__  = m(x1)

# Final model output is a 7-D vector with size `[dim, dim]`

