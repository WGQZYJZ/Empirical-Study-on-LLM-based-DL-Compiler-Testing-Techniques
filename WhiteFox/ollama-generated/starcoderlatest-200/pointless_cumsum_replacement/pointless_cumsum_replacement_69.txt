
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([x1.size()[0], 1, 64, 64], dtype=x1.dtype, layout=x1.layout, device=x1.device) # Create a tensor filled with the scalar value 1, with the specified dtype, layout, and device
        v2 = torch.convert_element_type(v1, x2.dtype) # Convert the elements of the tensor to the specified dtype
        v3 = torch.cumsum(v2, 0) # Compute the cumulative sum of the elements of the tensor along dimension 0
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(8, 64, 64) # Input 1 has size [8, 64, 64]
x2 = torch.randint_like(x1, high=10, dtype=torch.float32) # Input 2 has size [8, 64, 64]
