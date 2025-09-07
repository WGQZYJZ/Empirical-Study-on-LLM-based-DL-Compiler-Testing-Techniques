
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, inp) 
        if inp is None: 
            return v1
        else:
            return v1 + inp
 

# Initializing the model
m = Model()

 # Inputs to the model for 1st case - without keyword argument
x1 = torch.randn(50, 784)
inp = torch.randn(784, 239036)
 
__output__1 = m(x1, inp=None)
 
 # Inputs to the model for 2nd case - with keyword argument (different from previous one)
x1_kword = torch.randn(50, 784).cuda() 
__output__2 = m(x1_kword, inp=inp.cuda())

