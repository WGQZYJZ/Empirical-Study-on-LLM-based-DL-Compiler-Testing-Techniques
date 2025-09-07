
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v2 = torch.mm(x1,inp) # Matrix multiplication on two input tensors 
        v3  = v2 + inp # Add the result of the matrix multiplication to another tensor 'inp'
        return v3
 

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(5,4) # Input 1: a random 5 x 4 matrix  
inp = torch.ones(5,2)# Input 2 'inp' is one tensor with shape of [5 x 2]
__output__= m(x1, inp)
