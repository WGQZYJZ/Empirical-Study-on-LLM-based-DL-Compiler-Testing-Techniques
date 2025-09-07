
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device)
        return convert_element_type(v1 + torch.cumsum(convert_element_type(x1, dtype), dim=1), dtype)


# Initializing the model
m = Model()


