
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self):
        v0  = torch.full([2, 3], 1, dtype=torch.float32)
        v1  = convert_element_type(v0, torch.int8)
        v2  = torch.cumsum(v1, 1)
