
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1024, 512)
 
    def forward(self, x):
        v1  = self.linear(x) 
        v2  = torch.tanh(v1)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x  = torch.randn(500, 1024)
 
# Input to the model 
__output__   = m(x)