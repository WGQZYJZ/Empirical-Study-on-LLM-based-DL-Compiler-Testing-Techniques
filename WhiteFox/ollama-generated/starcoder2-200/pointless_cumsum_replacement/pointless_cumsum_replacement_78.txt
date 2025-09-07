
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, arg1, arg2):
        v1 = torch.full([arg1, arg2], 1, dtype=torch.double)
        v2 = convert_element_type(v1, torch.float64)
        v3 = torch.cumsum(v2, 1) 
        return v3


# Initializing the model