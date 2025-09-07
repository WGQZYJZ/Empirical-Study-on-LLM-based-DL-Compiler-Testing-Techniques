
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1  = torch.nn.Conv2d(3,8,5)
 
    def forward(self, x1):
        t4  = self.conv1(x1)
        t6 = torch.clamp_max(t4, max=0.7097932)
