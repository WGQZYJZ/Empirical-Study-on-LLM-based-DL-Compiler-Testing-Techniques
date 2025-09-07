
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0):
 
        t1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        v0 = convert_element_type(t1, dtype)
        v1 = torch.cumsum(v0, 1)
        
        return v1


# Initializing the model