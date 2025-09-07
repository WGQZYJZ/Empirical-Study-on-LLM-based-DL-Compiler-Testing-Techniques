
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.MM(False)
 
    def forward(self, x1, inp=0):
        v1  = self.mm(x1, inp) 
        return v1


# Initializing the model
m  = Model()

# Inputs to the model
input1 = torch.randn(32, 64, dtype=torch.double)
input2 = torch.randn(32, 50, 89, 75, dtype=torch.float)
__output__  = m(x1=input1, inp=input2)


# Description of the output
