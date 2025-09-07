
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
 
        v0  = torch.full([3], 256, dtype=torch.float) # Create a tensor filled with the scalar value 256 and with type torch.float
        v1  = convert_element_type(v0, torch.int32)  # Convert the elements of the tensor to the specified dtype
        
        v1 = torch.cumsum(v1, 0) # Compute the cumulative sum of the elements of the tensor along dimension 0
 
        return v1

# Initializing the model
m = Model()
 
# Inputs to the model
__output__  = m(torch.randn(3))

