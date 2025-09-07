
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([arg1, arg2], 0, dtype=dtype) # Create a tensor filled with the scalar value 0
        v2 = torch.cumsum(v1, dim=dim) # Compute the cumulative sum of elements of the tensor along dimension `dimension`
        return v2

# Initializing model
m = Model()
