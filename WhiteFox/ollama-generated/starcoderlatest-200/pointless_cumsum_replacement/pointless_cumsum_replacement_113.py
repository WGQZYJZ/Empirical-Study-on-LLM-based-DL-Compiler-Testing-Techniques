
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = convert_element_type(torch.full([x1.shape[0], x1.shape[1], x1.shape[2] + 1, x1.shape[3]], 1), x1.dtype)
        v2 = convert_element_type(torch.cumsum(v1, 1), x1.dtype)
        return v2

