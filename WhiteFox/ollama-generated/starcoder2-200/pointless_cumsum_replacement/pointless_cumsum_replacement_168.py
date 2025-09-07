
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        v2 = convert_element_type(v1, dtype)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn([50, 3])
x2  = torch.randn([784])
__output__  = m(x1, x2)

