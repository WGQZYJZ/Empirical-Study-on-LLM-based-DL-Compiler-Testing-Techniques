
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.leakyrelu = nn.LeakyReLU()
 
    def forward(self, x1):
         v1  = self.conv(x1)
         v2  = v1 > 0 
         v4 = torch.where(v2, v3, -0.05*v3) 
         return v4