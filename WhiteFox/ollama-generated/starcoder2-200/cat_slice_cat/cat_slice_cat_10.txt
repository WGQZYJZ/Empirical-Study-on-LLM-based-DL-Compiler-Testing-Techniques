
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x0):
       v1 = 0 
       for i in range(x0.__len__())
         v1 += v1
       return v6


# Initializing the model:
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(10*10*5, 64, 64)
__output__  = m([x1, x2])

