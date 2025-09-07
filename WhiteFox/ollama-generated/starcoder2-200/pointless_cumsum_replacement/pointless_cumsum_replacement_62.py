

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.full([256, 3], 1, dtype=dtype, layout=layout, device=device) # Create a tensor filled with the scalar value 1
        v2  = convert_element_type(v1, dtype) # Convert the elements of the tensor to the specified dtype
        v3  = torch.cumsum(v2, 1) # Compute the cumulative sum of the elements of the tensor along dimension 1
        return v3


# Initializing the model
m  = Model() 

# Inputs to the model
x1  = torch.randn(3, 64, 64)
