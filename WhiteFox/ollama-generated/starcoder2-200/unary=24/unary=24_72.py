
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1)

        self._negative_slope = negative_slope
    
    @torch.jit.ignore
    def __constants__(self): 
        return [self._negative_slope]

    def forward(self, x):
        v0 = self.conv(x)
        m = (v0 > 0).type_as(v0)

        v1 = -m * self._negative_slope * v0 + m * v0
        return torch.where(m, v0, v1)
