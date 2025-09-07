
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        v1  = torch.full([arg1, arg2], 1) 
        v2  = v1 * 0.7071067811865476
        v3  = convert_element_type(v2, 'float')
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randint(-99, -90, (387), dtype=torch.int64)
x2  = x1 // 5
__output__  = m(x1, x2)

