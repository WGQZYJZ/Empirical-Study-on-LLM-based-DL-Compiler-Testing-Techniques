
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([x1.shape[0], 256, 48, 48], 1, dtype=x1.dtype, layout=torch.Strided, device=x1.device, pin_memory=False)
        v2 = convert_element_type(v1, x1.dtype)
        v3 = torch.cumsum(v2, 1)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn([1, 3, 64, 64])
