
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([x1, x2], 1, dtype=x1.dtype, layout=x1.layout, device=x1.device) 
        v2 = convert_element_type(v1, x1.dtype) # Convert the elements of tensor `v1` to the specified type
        v3 = torch.cumsum(v2, 1) # Compute the cumulative sum of the elements of tensor `v2` along dimension 1
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, dtype=torch.float64, layout=torch.strided)
x2 = torch.randint(0, x1.numel(), [4], dtype=torch.int32, device=device, requires_grad=False) # Create a tensor of random values
