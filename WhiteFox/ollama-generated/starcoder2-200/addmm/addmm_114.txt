
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp) + 1.0
        return v1


# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(256, 384).type(torch.FloatTensor)
inp = torch.randn(384, 384).type(torch.FloatTensor)
 
__output__  = m(x1, inp=inp)

