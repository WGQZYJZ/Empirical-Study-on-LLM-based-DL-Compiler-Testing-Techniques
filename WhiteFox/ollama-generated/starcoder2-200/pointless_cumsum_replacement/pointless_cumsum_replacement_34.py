
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.full([x1, x2], 1)
        v2  = convert_element_type(v1, dtype='int')
        v3  = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = int(input())
x2  = int(input())
__output__  = m(x1, x2)