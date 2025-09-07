
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.full([x1.size()[0], 8], 1, dtype=x1.dtype, layout=x1.layout, device=x1.device, pin_memory=False) 
        t2 = convert_element_type(t1, x1.dtype)
        t3 = torch.cumsum(t2, 1)
        return t3


# Inputs to the model
x1 = torch.randn(10, 3, 64, 64)
x2 = torch.randint(0, 10, [1])
