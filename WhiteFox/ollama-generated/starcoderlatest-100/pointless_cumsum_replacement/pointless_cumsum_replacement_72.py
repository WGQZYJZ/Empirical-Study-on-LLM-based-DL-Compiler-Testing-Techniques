
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.full = torch.ones(1, 3, 64, 64, dtype=torch.int32)
 
    def forward(self, x1):
        v1 = torch.full([x1.shape[0], x1.shape[1], x1.shape[2], x1.shape[3]], 1, dtype=torch.int32) # Create a tensor filled with the scalar value 1, with the specified dtype, layout, and device
        v2 = torch.convert_element_type(v1, x1.dtype) # Convert the elements of the tensor to the specified dtype
        v3 = torch.cumsum(v2, dim=1) # Compute the cumulative sum of the elements of the tensor along dimension 1
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
