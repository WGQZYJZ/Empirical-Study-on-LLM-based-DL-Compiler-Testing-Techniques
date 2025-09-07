
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):
        v3 = torch.full([84000], 1, dtype=dtype, layout='SP', device=device) # Create a tensor filled with the scalar value 1 with the specified dtype and layout
        v7 = convert_element_type(v3, torch.float64) 
        v5 = torch.cumsum(v7, 0)
        return v5


# Initializing the model
m = Model()


# Inputs to the model
x2  = torch.randn([10])

__output__  = m(x2)
