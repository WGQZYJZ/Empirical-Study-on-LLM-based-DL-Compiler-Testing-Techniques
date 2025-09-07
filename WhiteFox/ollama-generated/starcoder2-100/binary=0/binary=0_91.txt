
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, t):
         v1 = self.conv(x1)
         v2 = v1 + t
         return v2


# Initializing the model
m = Model()
t = torch.randn(8).cuda()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64).cuda()
  __output__  = m(x1, t)

