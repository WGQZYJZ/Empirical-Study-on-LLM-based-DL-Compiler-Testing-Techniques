
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, arg1, arg2):
        x = torch.full([arg1, arg2], 1, dtype=torch.int64, layout=torch.strided, device='cpu', pin_memory=False)
        y = convert_element_type(x, torch.int32)
        z = torch.cumsum(y, 0)
        return z


# Inputs to the model
arg1 = 5
arg2 = 8
