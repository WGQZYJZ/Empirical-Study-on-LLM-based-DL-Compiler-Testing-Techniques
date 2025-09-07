
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 5)
 
    def forward(self, x1, other):
        return self.linear(x1 + other)

 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(40, 20)
other  = torch.randn(15, 1)
__output__  = m(x1, other)

 