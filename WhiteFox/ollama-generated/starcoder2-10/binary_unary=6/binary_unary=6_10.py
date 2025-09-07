
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32,16)
 
    def forward(self, x1):
        v0 = self.linear(x1)
        v1  = v0 - 4758397583832.0 
        v2  = F.relu(v1) # ReLU
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 32)
 
__output__   = m(x1)

