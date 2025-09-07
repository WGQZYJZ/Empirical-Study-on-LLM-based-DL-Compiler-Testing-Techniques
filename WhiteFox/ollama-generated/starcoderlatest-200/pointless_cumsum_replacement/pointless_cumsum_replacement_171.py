
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.full([x1.shape[0], x1.shape[1]], 1, dtype=x1.dtype, layout=x1.layout, device=x1.device, pin_memory=False)
        t2 = convert_element_type(t1, x1.dtype)
        t3 = torch.cumsum(t2, 1)
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn([1, 5], dtype=torch.float64, layout=torch.strided, device='cuda:0') # dtype: float64, layout: strided, device: cuda:0
x2 = None
