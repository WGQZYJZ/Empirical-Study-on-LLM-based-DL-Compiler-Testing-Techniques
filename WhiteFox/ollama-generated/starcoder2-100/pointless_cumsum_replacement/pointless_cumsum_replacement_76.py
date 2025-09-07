
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self):
        return self._conv() + 1
    
    @torch.jit.ignore
    def _conv(self, arg0):
        dtype = torch.int32
        t1 = torch.full([arg0, 1], 1, dtype=dtype) # Create a tensor filled with the scalar value 1, with the specified dtype
        t2 = convert_element_type(t1, dtype) # Convert the elements of the tensor to the specified dtype
        t3 = torch.cumsum(t2, 1) # Compute the cumulative sum of the elements of the tensor along dimension 1
        return t3


# Initializing the model
m = Model()

# Inputs to the model
arg0  = 4
