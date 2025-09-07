
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear  = torch.nn.Linear(10,2)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v3  = torch.tanh(v1) # Tanh function
        return v3


# Initializing the model
m = Model()
__output__  = m(torch.randn(4))
 
