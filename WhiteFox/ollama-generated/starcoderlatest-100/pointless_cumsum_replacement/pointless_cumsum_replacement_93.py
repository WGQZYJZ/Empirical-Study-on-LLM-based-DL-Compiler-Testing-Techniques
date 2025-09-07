
class Model(torch.nn.Module):
    def __init__(self, arg1, arg2):
        super().__init__()
        self.t1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
 
    def forward(self, x):
        t2 = convert_element_type(self.t1, dtype)
        t3 = torch.cumsum(t2, 1)
        return t3
# Initializing the model
m = Model(64, 100)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
