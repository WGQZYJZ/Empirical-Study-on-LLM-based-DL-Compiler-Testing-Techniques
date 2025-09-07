
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8, bias=True)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1
 
# Initializing the model
m = Model()
 

# Inputs to the model
x2 = torch.randn(30, 10)
__output__  = m(x2)

