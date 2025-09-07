
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = torch.full([x1, x2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False) 
        v2 = convert_element_type(v1, dtype) 
        v3 = torch.cumsum(v2, 1)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.tensor(64) # The first dimension of the input tensor is batch size, while the second and third dimensions are width and height
x2 = torch.tensor(64)
