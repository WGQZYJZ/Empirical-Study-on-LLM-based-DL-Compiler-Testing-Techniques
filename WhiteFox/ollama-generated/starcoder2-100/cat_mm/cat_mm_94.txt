
class Model(torch.nn.Module):
    def __init__(self, num):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
        self.drop = torch.nn.Dropout()
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        
        v2 = v1 * x2 + self.drop(v1)

        v3  = torch.cat([v2, v2], dim=0)
        return v3


# Initializing the model
m  = Model(num=7)


# Inputs to the model
x1  = torch.randn(16, 3, 50, 49)
 
input2  = x1 ** 2.8 + 2 - x1 * v1 
 
__output__  = m(x1, input2)

-rw-r--r-- 1 jovyan users   767 May  3 09:38 model.py
