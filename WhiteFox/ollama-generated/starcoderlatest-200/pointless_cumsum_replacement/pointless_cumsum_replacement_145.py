
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([x1.shape[0], 8, 64, 64], 1, dtype=x1.dtype, layout=x1.layout, device=x1.device, pin_memory=False)
        v2 = convert_element_type(v1, x2.dtype)
        v3 = torch.cumsum(v2, 1)
        return v3
 
