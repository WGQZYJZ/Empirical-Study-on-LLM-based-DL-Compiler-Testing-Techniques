
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.full  = torch.full([arg1, arg2], 1)
    
    def forward(self, x1):
        v1  = convert_element_type(self.full, dtype)
        v3  = torch.cumsum(v1, 1)
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn([arg1, arg2])
__output__  = m(x1)

