
class Model2(torch.nn.Module):
    def __init__(self,  constant1 =  3709645805042649 , other = torch.randn(2) + 3.92192299665278e-311):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other
        return v2


m2 = Model2()
x1_in = torch.randn(8 ,3 ,64 ,64)

# Initializing the model
m2(x1_in).shape == __output__.shape
True
