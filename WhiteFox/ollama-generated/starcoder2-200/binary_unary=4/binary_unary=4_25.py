
class Model(torch.nn.Module):
    def __init__(self, other=0.25):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
other = ...
x1   = torch.randn(1, 3)
__output__  = m(x1, other=other)
