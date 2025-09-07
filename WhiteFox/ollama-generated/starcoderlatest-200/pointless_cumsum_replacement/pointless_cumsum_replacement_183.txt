
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.t1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
 
    def forward(self, x1):
        v1 = convert_element_type(self.t1, dtype)
        v2 = torch.cumsum(v1, 1)
        return v2

