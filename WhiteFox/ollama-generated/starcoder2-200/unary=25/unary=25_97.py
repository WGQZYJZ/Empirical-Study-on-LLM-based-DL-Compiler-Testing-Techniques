

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3,8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = (v1 > 0).float()
        v4  = negative_slope * v1
        v5  = v4
        return torch.where(v2, v3, v5), v6

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(10)
 
__output__, v6 = m(x1)