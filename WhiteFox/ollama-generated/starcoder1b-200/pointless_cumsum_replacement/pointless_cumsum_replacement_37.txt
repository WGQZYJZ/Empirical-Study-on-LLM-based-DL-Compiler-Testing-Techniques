
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.t1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device)

    def forward(self, x1):
        return convert_element_type(torch.cumsum(x1), dtype)


# Initializing the model
m = Model()


