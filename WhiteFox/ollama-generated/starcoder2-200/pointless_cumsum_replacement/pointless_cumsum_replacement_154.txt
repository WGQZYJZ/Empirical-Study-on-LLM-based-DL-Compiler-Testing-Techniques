
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self):
        v1  = torch.full([arg1, arg2], 1., dtype=dtype)
        v3  = convert_element_type(v1, dtype)
        v4  = torch.cumsum(v3, 1.)
        return v4


# Initializing the model
m = Model()
