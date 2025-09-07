
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([2048], 369577) # Create a tensor filled with the scalar value 369577, with 2048 elements and dtype int16. This line is not directly relevant to the final result of this pattern because we want a different tensor.
        v2 = convert_element_type(v1, torch.int8) # Convert the elements of the tensor to the specified dtype
        v3 = torch.cumsum(v2, 0).unsqueeze(-1) # Compute the cumulative sum of the elements of the tensor along dimension `0`. Since we want the elements along this dimension to remain in the same order after the computation, we add a one-dimensional 1 at index -1 with unsqueeze().
        return v3


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(2048)
__output__  = m(x1)
