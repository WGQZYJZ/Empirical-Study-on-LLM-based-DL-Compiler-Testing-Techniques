
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, dtype, layout, device):
        v1 = torch.full([x1.shape[0], x1.shape[1]], 1, dtype=dtype, layout=layout, device=device) 
        v2 = convert_element_type(v1, dtype) 
        v3 = torch.cumsum(v2, dim=1)
        return v3


# Input tensor to the model
x1 = torch.randn(1, 3, 64, 64)

