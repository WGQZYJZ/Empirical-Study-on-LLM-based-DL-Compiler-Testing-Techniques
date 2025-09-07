
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(48,10)
    
    def forward(self, x1):
        v1  = self.linear(x1) #Apply a linear transformation to the input tensor
        return v1 + other
    
# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(320,48)
other = torch.randn(320,) * 5
__output__= m(x1)

