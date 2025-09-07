
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.l1 = torch.nn.Linear(20, 30)
        self.act = torch.nn.ELU()
 
    def forward(self, x):
        v1 = self.l1(x) 
        v2 = self.act(v1 + 3).clamp_min_(0.).clamp_max_(6.)
        v4 = v2 / 6
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(5, 20) # generate some input
__output__  = m(x)
