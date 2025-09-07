
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.full([x1.shape[0], x1.shape[2] * x1.shape[3]], 1, dtype=x1.dtype, layout=x1.layout, device=x1.device)
        v2  = convert_element_type(v1, self.v1.dtype)
        v3  = torch.cumsum(v2, dim=1)
        return v3


