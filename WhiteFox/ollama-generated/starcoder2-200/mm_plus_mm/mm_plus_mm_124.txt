
class Model(torch.nn.Module):
    def __init__(self, m1, m2, m3):
        super().__init__()
        self.m1 = torch.nn.Linear(in_features=m1, out_features=m1)
        self.m2  = torch.nn.Linear(in_features=m2, out_features=m1*m2)
    
    def forward(self, x):
        v1  = self.m1(x)
        v3  = self.m2(v1) 
        return v3


# Initializing the model
m  = Model(10, 5, 8)

# Inputs to the model
x1  = torch.randn(10, 5)
x2  = torch.randn(10,)
__output__  = m(x1)

