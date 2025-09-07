
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 8)
 
    def forward(self, x1): 
        v1  = self.linear(x1)  
        return torch.tanh(v1)


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(100, 32) 
 # Output of the model (for evaluation purposes only -- do not actually evaluate!)
__output__  = m(x1)
