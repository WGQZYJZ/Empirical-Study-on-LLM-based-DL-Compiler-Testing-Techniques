
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1

 # Initializing the model
m = Model()
other = -2

# Inputs to the model
x1  = torch.randn(50, 3)
 
__output__  = m(x1)
 
 