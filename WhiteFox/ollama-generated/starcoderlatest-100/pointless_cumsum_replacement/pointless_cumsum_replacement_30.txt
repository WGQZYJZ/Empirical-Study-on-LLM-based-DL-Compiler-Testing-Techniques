
class Model(torch.nn.Module):
    def __init__(self, arg1=5, arg2='long'):
        super().__init__()
 
        self.t1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
 
    def forward(self):
        v1 = convert_element_type(t1, dtype)
        v3 = torch.cumsum(v1, 1)
        return v6
