
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([x1.shape[0], 8], 1, dtype=x1.dtype) # Create a tensor filled with the scalar value 1, with the specified dtype and device 
        v2 = convert_element_type(v1, x1.dtype) # Convert the elements of the tensor to the specified dtype
        v3 = torch.cumsum(v2, 0) # Compute the cumulative sum of the elements of the tensor along dimension 0
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(64, 64, dtype=torch.float32)
