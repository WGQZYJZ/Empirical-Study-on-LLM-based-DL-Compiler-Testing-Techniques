
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()

        self._dim = dim
        self.linear1  = torch.nn.Linear(3200, 4)
        self.conv  = torch.nn.Conv2d(8, 64, 7, padding=3)
 
    def forward(self, x):
        
        v1 = torch.addmm(x, mat1, mat2)
        v2 = torch.cat([v1], self._dim)

        return v2

# Initializing the model
m  = Model(0)

 # Inputs to the model
x1  = torch.randn(8, 3, 48, 64)

 __output__= m(x1)
