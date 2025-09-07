
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, arg1, arg2, **kwargs):
        v1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        return convert_element_type(v1, dtype)


# Inputs to the model
x1 = [4, 7]
