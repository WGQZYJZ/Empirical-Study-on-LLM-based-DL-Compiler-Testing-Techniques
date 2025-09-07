
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.full([25600], 1, dtype=x1.dtype)
        v2  = torch.convert_element_type(v1, x1.dtype)
        v3  = torch.cumsum(v2, 1)
        return v3

# Initializing the model