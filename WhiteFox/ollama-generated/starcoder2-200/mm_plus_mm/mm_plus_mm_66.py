

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm1  = torch.nn.Linear(20, 4)
        self.mm2  = torch.nn.Linear(35, 8)
 
    def forward(self, x1, x2):
        v1  = self.mm1(x1)
        v2  = self.mm2(v1)
        v3  = v2 + v1
        return v3

# Initializing the model
m  = Model()
 
# Inputs to the model
x1, x2 = torch.randn(50, 20), torch.randn(49, 35)
 
 