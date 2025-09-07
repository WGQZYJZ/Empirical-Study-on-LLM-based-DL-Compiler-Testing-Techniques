
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(8, 16)
 
    def forward(self, x2, other=0):
        v7 = self.linear(x2)
        v9 = v7 + other # Here is the change!
        v10 = torch.relu(v9)
        return v10

m  = Model()

 # Inputs to model
x2 = torch.randn(1, 8)
 
 ## This is an example of calling `Model` with keyword arguments.
__output__  = m(x2, other=torch.randn(1))
