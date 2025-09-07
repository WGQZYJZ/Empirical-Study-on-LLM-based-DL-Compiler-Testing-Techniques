
class Model(torch.nn.Module):
    def __init__(self, dtype=torch.float32, layout=torch.strided, device="cpu", pin_memory=False):
        super().__init__()
        self.tensor = torch.full([8, 1], 1, dtype=dtype, layout=layout, device=device, pin_memory=pin_memory)
 
    def forward(self, x1, x2):
        t1 = torch.full([x1.shape[0], x2.shape[1]], 1, dtype=torch.float32, layout=torch.strided, device="cpu", pin_memory=False)
        t2 = convert_element_type(t1, x1.dtype)
        t3 = torch.cumsum(t2, 1)
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 8, dtype=torch.int64)
x2 = torch.randn(8, 1)
