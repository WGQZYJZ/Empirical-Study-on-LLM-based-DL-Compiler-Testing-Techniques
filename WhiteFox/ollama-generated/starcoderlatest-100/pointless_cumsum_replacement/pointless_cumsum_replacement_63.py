
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.full([x1.shape[0], 1], 1, dtype=x1.dtype, device=x1.device) # Create a tensor filled with the scalar value 1, with the specified dtype and device
        t2 = convert_element_type(t1, x1.dtype) 
        t3 = torch.cumsum(t2, 1)
        return t3


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 64, 64)
x2 = torch.randn(1, 8, 32, 32)
