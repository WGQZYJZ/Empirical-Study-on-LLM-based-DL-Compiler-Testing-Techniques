
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.full([320], 1, dtype=torch.float) 
        v2  = convert_element_type(v1, torch.float64)  
        v3  = torch.cumsum(v2, 0) 
        return v3


# Initializing the model