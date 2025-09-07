
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([x1], 1, dtype=torch.float32) # Create a tensor filled with the scalar value 1, with dtype=float32
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, 0) # Compute the cumulative sum of the elements of the tensor along dimension 0
        return v3


# Inputs to the model
x1 = torch.randn(4, dtype=torch.int64)
x2 = torch.randn(5, dtype=torch.float32)
