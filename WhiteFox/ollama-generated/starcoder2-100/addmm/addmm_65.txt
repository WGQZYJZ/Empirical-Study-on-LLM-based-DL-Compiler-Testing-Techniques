
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None): 
        v1 = torch.mm(x1, inp) 
        return v1 + 5


# Initializing the model
m = Model()

# Inputs to the model
inp_tensor  = torch.randn(20,34)
x1  = torch.randn(17,19)
__output__  = m(x1, inp=inp_tensor)

