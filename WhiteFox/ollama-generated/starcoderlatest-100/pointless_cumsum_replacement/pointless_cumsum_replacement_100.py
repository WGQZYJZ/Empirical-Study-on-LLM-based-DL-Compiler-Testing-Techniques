
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, dtype=torch.float32, layout=None, device=None, pin_memory=False):
        t1 = torch.full([x1, x2], 1, dtype=dtype, layout=layout, device=device, pin_memory=pin_memory)
        t2 = convert_element_type(t1, dtype)
        t3 = torch.cumsum(t2, 1)
        return t3
 
 # Inputs to the model
x1 = 6
x2 = 7
