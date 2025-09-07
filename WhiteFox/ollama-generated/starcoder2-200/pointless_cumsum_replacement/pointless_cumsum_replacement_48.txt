
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg0, arg1):
        v1  = torch.full([arg1, arg2], 1) # Create a tensor filled with the scalar value 1
        v2  = convert_element_type(v1, dtype=dtype, layout=layout, device=device, pin_memory=False) # Convert the elements of the tensor to the specified dtype and set pin_memory to false. Note that the parameter is named pin_memory instead of pinned_memory because this is the official parameter name in the PyTorch APIs.
        v3  = torch.cumsum(v2, 1) # Compute the cumulative sum of the elements of the tensor along dimension 1. The value of argument dim is set to -1 since PyTorch will always return a one-dimensional tensor if you specify both dim and keepdim as True.
        return v3


# Initializing the model