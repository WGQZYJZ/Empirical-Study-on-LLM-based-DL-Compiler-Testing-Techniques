
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)


