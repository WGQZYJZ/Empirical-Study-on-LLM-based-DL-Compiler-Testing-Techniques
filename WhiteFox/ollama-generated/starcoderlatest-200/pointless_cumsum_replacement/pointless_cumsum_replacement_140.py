
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.full([3, 3], 0.5)
        t2 = convert_element_type(t1, dtype=x1.dtype)
        t3 = torch.cumsum(t2, dim=-1)
        return t3


# Initializing the model
m = Model()

# Inputs to the model
arg1 = x1.size(-1)
arg2 = 16
dtype = torch.float
layout = torch.strided
device = torch.cpu
pin_memory = False
x1 = torch.randn(3, 1024).to("cuda:2")
x2 = x1.size(-1)
