
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = torch.full([x1.shape[0], x2.shape[1]], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, 1)
        return v3


# Input data for the model
x1 = torch.randn(4, 5)
x2 = torch.randint(0, 10, (3, 6))
x3 = torch.arange(8).view(2, 2, 2).transpose(-1, -2).reshape([2, -1])
