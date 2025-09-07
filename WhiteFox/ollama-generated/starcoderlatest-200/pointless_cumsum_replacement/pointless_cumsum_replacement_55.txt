
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3, x4, x5):
        v1 = torch.full([x1, x2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False) 
        t1 = convert_element_type(v1, dtype)
        v2 = torch.cumsum(t1, 1)


# Inputs to the model
x1 = torch.randn((5,), dtype=torch.long)
x2 = torch.randn((3,), dtype=torch.float64)
