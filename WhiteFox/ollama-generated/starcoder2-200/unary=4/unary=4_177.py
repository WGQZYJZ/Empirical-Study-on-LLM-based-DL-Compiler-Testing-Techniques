
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(8, 10)
 
    def forward(self, x2):
        v7  = self.linear(x2)
        v9  = v7  * 0.5
        v10  = v7  * 0.7071067811865476
        v13  = torch.erf(v10)
        v17  = v13  + 1 
        v29  = v9  * v17
        return v29

# Initializing the model
m = Model()

# Inputs to the model
x2  = torch.randn(1, 8)
__output__  = m(x2)

