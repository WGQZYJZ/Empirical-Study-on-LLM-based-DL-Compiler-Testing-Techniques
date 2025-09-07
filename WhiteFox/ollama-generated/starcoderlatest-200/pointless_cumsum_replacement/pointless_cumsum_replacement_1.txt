
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.t1 = torch.full([2, 3], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
 
    def forward(self, x1):
        t2 = convert_element_type(self.t1, dtype)
        t3 = torch.cumsum(t2, 1)
        return t3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
