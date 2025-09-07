
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.t1 = torch.full([8], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
 
    def forward(self, x2):
        t1 = self.t1
        t2 = convert_element_type(t1, dtype)
        t3 = torch.cumsum(t2, 1)
        return t3


# Inputs to the model
x2 = torch.randn(1, 8, 64, 64)
