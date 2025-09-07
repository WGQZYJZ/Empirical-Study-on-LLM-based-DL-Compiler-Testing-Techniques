
class Model(torch.nn.Module):
    def __init__(self, arg1=0, arg2='foo', dtype=torch.int64, layout='NCHW', device='cpu', pin_memory=False):
        super().__init__()
 
    def forward(self):
        v1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=pin_memory)
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, 1)
        return v6


# Expected input tensor
arg1 = (10, )
arg2 = (5, )
dtype = torch.float32
layout = 'NCHW'
device = 'cuda:0'
pin_memory = False
