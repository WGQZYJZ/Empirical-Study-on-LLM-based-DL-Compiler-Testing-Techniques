
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.full = torch.nn.Parameter(torch.ones([2, 3], dtype=dtype))
    
    def forward(self, x1):
        v1 = convert_element_type(x1, self.full)
        v2 = torch.cumsum(v1, 1)

# Initializing the model
m = Model()


# Inputs to the model
t1 = torch.randn([3], dtype=dtype)
__output__  = m(t1)