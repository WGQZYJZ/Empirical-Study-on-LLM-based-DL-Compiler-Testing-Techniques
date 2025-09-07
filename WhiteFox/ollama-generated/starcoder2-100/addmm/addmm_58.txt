
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp)
        return v1 + inp
 
 # Initializing the model
m  = Model()

 # Inputs to the model
input1 = torch.randn(2048, 512)
input2 = torch.randn(512, 64)
inp = input1
 
__output__  = m(input1, inp=input2)