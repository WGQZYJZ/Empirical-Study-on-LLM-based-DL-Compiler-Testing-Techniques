
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = torch.full([x1], 1) # Create a tensor filled with the scalar value 1, with size 4 in the first dimension and 10 along other dimensions (size of 4 x 5 x 6), using dtype float32, layout NCHW and device cpu
        v1  = v2 * 0.7928758 # Multiply the output by 0.7928758
        v3  = torch.cumsum(v1, dim=dim)  # Compute the cumulative sum of the elements of the tensor along dimension 'dim' 
        return v3


# Initializing the model
m = Model()


# Inputs to the model