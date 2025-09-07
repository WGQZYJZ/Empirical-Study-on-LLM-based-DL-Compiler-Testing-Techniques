
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.split = torch.split
        self.concat  = torch.cat
        self.dim = dim

    def forward(self, x1):
        v2 = self.split(x1, [5], self.dim) 
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(30)
__output__  = m(x1)
 
