
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v5 =  v4 * 0.7071067811865476
        v9 = torch.erf(v8) 
        return v2 + 1
