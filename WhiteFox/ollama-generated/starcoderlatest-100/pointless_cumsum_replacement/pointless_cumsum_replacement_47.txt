
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, arg1, arg2):
        v1 = torch.full([arg1, arg2], 1, dtype=x1.dtype, layout=x1.layout, device=x1.device)
        v2 = convert_element_type(v1, x2.dtype)
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn([10, 5])
x2 = torch.float64
arg1 = (x1.size()[0], x2.size()[0])
arg2 = x1.size()[1]
