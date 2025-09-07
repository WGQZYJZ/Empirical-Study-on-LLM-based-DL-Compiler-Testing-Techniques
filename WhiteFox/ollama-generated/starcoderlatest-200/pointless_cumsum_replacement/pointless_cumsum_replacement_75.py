
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t1, arg2, device):
        v1 = torch.full([t1], 1, dtype=dtype, layout=layout, device=device)
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, 1)
        return v6
# Initializing the model
m = Model()


# Inputs to the model
t1 = torch.randn(1, 8, 1024, 64)
arg2 = 'float'
device = 'cuda:0'
