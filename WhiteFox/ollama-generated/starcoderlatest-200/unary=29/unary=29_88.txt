
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, min_value=0., max_value=1.):
        v1 = F.conv2d(x1, self.conv, bias=None, stride=1, padding=0, dilation=1, groups=1)
        v2 = torch.min(v1, dim=-1, keepdim=False)[0]
        v3 = torch.max(v2, dim=-1, keepdim=True)[0]
        return v3


# Initializing the model
m = Model()
