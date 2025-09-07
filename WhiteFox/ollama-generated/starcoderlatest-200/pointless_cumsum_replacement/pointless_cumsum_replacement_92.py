
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        t1 = torch.full([x1, x2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        t2 = convert_element_type(t1, dtype)
        t3 = torch.cumsum(t2, 1)
        return None

# Inputs to the model
x1 = 64 # the shape of input x1 should be (1, 64)
x2 = 80 # the shape of input x2 should be (2, 32)
