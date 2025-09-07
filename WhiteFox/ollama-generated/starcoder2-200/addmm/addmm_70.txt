
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, inp):
        v = torch.mm(input1, input2) + inp
        return v
        

# Initializing the model
m  = Model()

 # Inputs to the model
inp  = torch.randn(3,)
x1  = torch.randn(3, 4), x2  = torch.randn(4,5))
 
__output__  = m(input1=x1, input2=x2)