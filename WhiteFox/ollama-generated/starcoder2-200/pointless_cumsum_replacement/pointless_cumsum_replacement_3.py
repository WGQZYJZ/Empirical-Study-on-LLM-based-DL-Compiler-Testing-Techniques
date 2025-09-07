
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x207, x365):
        v4 = torch.full([arg1], 1, dtype=dtype)
        v5 = convert_element_type(v4, x365[0])
        v6 = torch.cumsum(v5, 1)
