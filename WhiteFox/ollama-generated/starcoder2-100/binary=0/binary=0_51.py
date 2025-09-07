
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1

class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1): 
        v2  = self.conv(x1) + torch.randn(v2.size())
        return v2


m_orig  = Model()
m       = Model2()


# Initializing the model
m0 = m_orig() # initial model (before training)
m1, m2   = m(x1), m(x1) # new models and their outputs after training.

