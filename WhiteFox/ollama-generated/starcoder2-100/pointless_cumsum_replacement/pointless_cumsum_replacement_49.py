
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self):
        v1  = torch.full([2, 3], 1) # Create a tensor filled with the scalar value 1
        v2  = convert_element_type(v1, 'float64') # Convert the elements of the tensor to the specified dtype
        v3  = torch.cumsum(v2, 1) # Compute the cumulative sum of the elements of the tensor along dimension 1
 
        return v3


# Initializing the model