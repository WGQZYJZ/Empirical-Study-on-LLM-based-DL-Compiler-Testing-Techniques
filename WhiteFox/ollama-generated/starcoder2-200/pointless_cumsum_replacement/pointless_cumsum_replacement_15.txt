
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.zeros([256], dtype=dtype) # Create a tensor filled with the scalar value 0 of the same size as input `x1` and the specified dtype
        v1  = convert_element_type(v0, dtype)
        v2  = torch.cumsum(v1, dim=-1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
input_1  = torch.randn([256], dtype=dtype)
__output__  = m(input_1)

