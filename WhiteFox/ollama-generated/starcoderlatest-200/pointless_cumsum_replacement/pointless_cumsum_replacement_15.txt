
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, arg1, arg2, dtype, layout, device):
        t1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        t2 = convert_element_type(t1, dtype)
        t3 = torch.cumsum(t2, 1)
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 3, 64, 64)
arg1 = x1.shape[0]
arg2 = x1.shape[2]
dtype = "float32"
layout = None
device = "cuda:0"

