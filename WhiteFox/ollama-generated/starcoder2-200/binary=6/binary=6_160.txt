
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v2  = self.linear(x1) 
        v4  = torch.zeros_like(v2)
        v5  = v2 - v4
        return v5


# Initializing the model
m = Model()
__output__  = m(x1)

