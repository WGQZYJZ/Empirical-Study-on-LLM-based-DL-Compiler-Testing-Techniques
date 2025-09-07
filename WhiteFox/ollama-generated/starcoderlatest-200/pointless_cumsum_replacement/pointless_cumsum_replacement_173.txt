
class Model(torch.nn.Module):
    def __init__(self, n1):
        super().__init__()
        self.n1 = n1
 
    def forward(self, x1):
        v1  = torch.full([self.n1, self.n1], 1, dtype=dtype, layout=layout, device=device, pin_memory=False) 
        t2  = convert_element_type(v1, dtype)
        t3  = torch.cumsum(t2, 0)
        return t3


# Inputs to the model
x1 = torch.randn(n1)
