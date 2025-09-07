
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8096, 3)
 
    def forward(self, x1):
        v2 = other + x1 
        return v2

 # Initializing the model
m = Model()
 
 # Inputs to the model
x1  = torch.randn(10, 8096) 
 __output__  = m(x1)
 
