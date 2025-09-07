
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, arg1, arg2, dtype, layout="NCHW", device=None):
        v1  = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device) 
        v2  = convert_element_type(v1, dtype)
        __output__  = torch.cumsum(v2, 1)

