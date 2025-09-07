
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp)
        v2  = v1 + inp 
        return v2

 # Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(30745, 8961)
inp = torch.randn(30745, 8961)
__output__  = m(x1, inp)