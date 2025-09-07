
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self._weight  = torch.nn.Parameter(data=0.5 * torch.ones_like([4]))
 
    def forward(self): # __init__()
        self.conv()
        other = 0.7071067811865476
        v2 = other
        v3 = torch.randn(1) 
        t4  = 1.119e-06
        v2_1  = v3 / (v2 + t4)
        v2 = other
        v3 = torch.randn(1, 48) # 1 * 48
        t5  = -1.1715e+03
        v6  = torch.sigmoid(t5)
        v7 = self._weight
        v9  = v2 + v7
        v9 += other * v9
        v10  = torch.relu(v9)
#        v4 = torch.empty_like(v9, out=None) # v10
#        v3  = v5 - 1

        v8 = t2_1 * 7
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x  = torch.randn(1, 48) # 1*48

 