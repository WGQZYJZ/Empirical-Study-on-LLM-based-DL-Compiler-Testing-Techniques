
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, arg1, arg2):
        v1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, 1)
        return v3


# Inputs to the model
arg1 = 8
arg2 = 7
