
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2, dtype=torch.float64, layout=torch.strided, device='cuda:0'):
        t1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False) 
        t2 = convert_element_type(t1, dtype) 
        t3 = torch.cumsum(t2, 1)
        return t3


# Initialization of the model
m = Model()

# Inputs to the model
x = (64, 3)
arg1, arg2 = x
