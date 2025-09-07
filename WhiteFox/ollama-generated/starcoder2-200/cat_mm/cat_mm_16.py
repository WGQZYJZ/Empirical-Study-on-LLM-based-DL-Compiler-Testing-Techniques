
class Model(torch.nn.Module):
    def __init__(self, num):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
        self.num  = num
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = t.mm(v1, v1)
        v3 = torch.cat([v2] * self.num, dim=-1).view(-1, v2.shape[0], 8 * self.num) 
        return v3

# Initializing the model
m  = Model(2)

 # Inputs to the model
x1  = torch.randn(5, 3, 64, 64)
 
 