
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, self.weight) # Matrix multiplication with weight
        v2  = torch.mm(v1, inp)# Matrix multiplication on the result of matrix multiplication above and another tensor 'inp'
        return v2
 

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(64, 5) # A randomly initialized tensor of shape (64 x 5).
inp  = torch.ones(5, 7)# A randomly initialized tensor of shape (5 x 7).
__output__  = m(x1, inp=inp)

