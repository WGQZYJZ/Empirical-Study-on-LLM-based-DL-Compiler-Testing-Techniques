
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = v1 + other # The `other` tensor is passed as a keyword argument here
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3)
other  = torch.randn(1, 8).cuda() # The `other` tensor is passed as a keyword argument here.
__output__  = m(x1)