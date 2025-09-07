
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, arg1, arg2, dtype=None, layout=None, device=None, pin_memory=False):
        v1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=pin_memory)
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, 1)
        return v3

# Initializing the model
m = Model()


# Inputs to the model
arg1 = 500
arg2 = 500
