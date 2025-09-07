
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, arg1, arg2, device=None, dtype=None, layout=None, pin_memory=False):
        m = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=pin_memory)
        v = convert_element_type(m, dtype)
        c = torch.cumsum(v, 1)
        return c


# Initializing the model
m = Model()


