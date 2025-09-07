
class Model(torch.nn.Module):
    def __init__(self, input1=None, input2=None):
        super().__init__()
        self._conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1, x2):
v1 = self._conv(x1)
        v2 = v1.cuda()
        v3 = self._conv(x2).cuda()
        return torch.mm(v2, v3),

