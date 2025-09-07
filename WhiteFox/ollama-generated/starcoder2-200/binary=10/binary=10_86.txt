
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=2):
        v1 = torch.nn.Linear(x1)
        v2 = v1 + other
        return v2
 
# Initializing the model
m  = Model()
 
 # Inputs to the model
x1 = torch.randn(3,)
other  = 4.5 
 __output__= m(x1, other=other)
