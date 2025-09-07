
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, dtype=torch.float32):
        v1 = torch.full([x1, x2], 1, dtype=dtype)
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, 1)
        return v6


# Inputs to the model
x1 = 4
x2 = 5
