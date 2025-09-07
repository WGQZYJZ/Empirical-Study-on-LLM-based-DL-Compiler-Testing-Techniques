
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)
        v2 = torch.gt(v1, 0).float()
        v3 = v1 * negative_slope
        v4 = torch.where(v2 == 1., v1, v3)
        return v4
