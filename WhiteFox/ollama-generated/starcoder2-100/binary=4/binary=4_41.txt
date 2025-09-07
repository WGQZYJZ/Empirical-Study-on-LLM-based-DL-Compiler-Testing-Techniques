
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20,1)
 
    def forward(self, x):
        y  = self.linear(x)
        return y + other

 # Initializing the model
m  = Model()

 # Inputs to the model
x  = torch.randn(32, 4*56*56)
other  = torch.ones(1, 1)
 
 __output__  = m(x)
