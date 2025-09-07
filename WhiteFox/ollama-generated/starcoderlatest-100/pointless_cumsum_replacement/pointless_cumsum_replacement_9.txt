
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, arg1=256, arg2=-1, dtype=torch.int8, layout='sparse', device='cpu', pin_memory=False):
        t1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=pin_memory)
        t2 = convert_element_type(t1, dtype)
        t3 = torch.cumsum(t2, 1)
        return t3


# Input tensor
x1 = torch.randn(1, 3, 64, 64).to('cuda')
