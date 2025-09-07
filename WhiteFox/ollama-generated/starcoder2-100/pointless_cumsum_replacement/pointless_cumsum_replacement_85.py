
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):

        v2  = torch.full([30], 5, dtype=dtype)
        v3  = convert_element_type(v2, dtype) # Convert the elements of the tensor to the specified dtype
        return torch.cumsum(v3, 1)

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(50, 784)

__output__  = m(x1)
