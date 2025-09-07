
class Model(torch.nn.Module):
    def __init__(self, arg1, arg2):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([arg1, arg2], 1)
        v2 = convert_element_type(v1, dtype=dtype) 
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model