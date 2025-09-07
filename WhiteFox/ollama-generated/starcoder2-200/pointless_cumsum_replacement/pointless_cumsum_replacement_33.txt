
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([32, 3], 1, dtype=x1.dtype) # Create a tensor filled with the scalar value 1 in the specified data type. It is important that the type of each element matches that of `x1`.
        v2 = convert_element_type(v1, x1.dtype) # Convert elements to their specified type using torch.Tensor.convert_element_type() method or torch.Tensor.to() method (depending on the version used)
        v3 = torch.cumsum(v2, 1).to(x1.device) # Compute the cumulative sum along dimension 1 of the elements in v2 using torch.Tensor.torch.cumsum() method. The resulting values are stored at v3. This value is re-casted to x1.dtype and then used as an argument for the conversion step
        return v3


# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(2, 3) 
 