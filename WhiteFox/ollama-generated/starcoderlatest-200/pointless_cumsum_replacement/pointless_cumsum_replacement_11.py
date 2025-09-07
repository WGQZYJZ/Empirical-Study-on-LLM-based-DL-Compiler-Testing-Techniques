
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.t1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
 
    def forward(self):
        v3 = convert_element_type(self.t1, dtype)
        v4 = torch.cumsum(v3, 1)
        return v4


# Inputs to the model
x1 = torch.randn(20, 3, 64, 64)
