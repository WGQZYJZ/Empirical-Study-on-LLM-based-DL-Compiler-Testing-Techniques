
class Model(torch.nn.Module):
    def __init__(self, dtype=None, layout=None, device=None, pin_memory=False):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([x1.shape[0], 8], 1.0, dtype=dtype, layout=layout, device=device, pin_memory=pin_memory)
        t2 = convert_element_type(v1, dtype)
        t3 = torch.cumsum(t2, 1)
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 64, 64)
x2 = torch.randint(0, 8, (1,)).item()
