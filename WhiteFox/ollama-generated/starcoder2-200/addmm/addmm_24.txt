
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.functional.linear
 
    def forward(self, x1, inp):
        v1  = self.mm(x1, x2)
        return v1 + inp


# Initializing the model
m  = Model()
 
 # Inputs to the model
x1 = torch.randn(3, 50, requires_grad=True)
x2 = torch.randn(50, 1800, requires_grad=True)
inp = torch.randn(3000, requires_grad=True)

 # Calling the model
__output__  = m(x1, inp)


