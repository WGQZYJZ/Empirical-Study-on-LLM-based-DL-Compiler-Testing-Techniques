
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.addmm = torch.nn.Linear(16, 8, bias=True)
 
    def forward(self, x1):
        t1 = torch.addmm(x1, m1, m2)
        t2 = torch.cat([t1], dim)
        return t2


# Initializing the model
m = Model()
dim = 0 # The dimension along which the result should be concatenated

# Inputs to the model
x1 = torch.randn(1, 8, 4, 4)
