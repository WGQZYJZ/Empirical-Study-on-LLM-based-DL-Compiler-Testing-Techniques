
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        t1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False) 
        t2 = convert_element_type(t1, dtype)
        t3 = torch.cumsum(t2, 1)
        return t3


# Inputs to the model
x1 = torch.randn([1], dtype=torch.float64, device='cuda', requires_grad=False)
x2 = torch.randn([1, 8], dtype=torch.int32, layout=torch.strided, device='cuda', pin_memory=True)
