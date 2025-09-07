
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.full([x1, x2], 1, dtype=dtype)
        v3  = convert_element_type(v1, dtype) 
        return v3

# Initializing the model