
class Model2(torch.nn.Module):
    def __init__(self, other_t: torch.Tensor = None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if other_t is not None:
            self.other_t = nn.Parameter(torch.FloatTensor(other_t))
 
    def forward(self, x1):
        v1 = self.conv(x1)
        if self.other_t is not None:
            v2 = v1 + self.other_t
        else:
            v2 = v1 
        return v2

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
m2 = Model2()
