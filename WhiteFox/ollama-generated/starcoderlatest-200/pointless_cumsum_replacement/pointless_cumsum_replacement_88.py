
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.full([x1.shape[0], 8], 1)
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, dim=1)
# 