
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(2, 8)
 
    def forward(self, x1, other=None):
        v1  = self.lin(x1)
        if other is None:
            return v1
        else:
            v3 = v1 + other
            v4  = torch.nn.functional.relu(v3) 
            return v4


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 2)
__output__  = m(x1)

