
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.mm
 
    def forward(self, x1, inp):
        v2  = mm(x1, inp) + inp
        return v2

 # Initializing the model
 m = Model()
 
# Inputs to the model
input1  = torch.randn(5,3)
input2  = torch.randn(3,4)
inp = input1 + 0.789
