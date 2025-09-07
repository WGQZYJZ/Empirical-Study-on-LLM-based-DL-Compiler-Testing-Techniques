
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(3, 1)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = v1 - other
        return v2


# Initializing the model
m = Model()
__output__  = m(x1) # 'other' is a tensor (not a scalar)

