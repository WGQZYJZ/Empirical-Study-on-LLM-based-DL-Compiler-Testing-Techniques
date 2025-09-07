
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, arg1, arg2):
        v1 = torch.full([arg1, arg2], 1)
        v2 = torch.ops.aten.convert_element_type(v1, arg3)
        v4 = torch.cumsum(v2, axis=axis).squeeze()


# Initializing the model