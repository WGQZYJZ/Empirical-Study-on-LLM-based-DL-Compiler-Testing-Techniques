
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1,inp) 
        return v1 + 1 
 
 
# Initializing the model with a predefined tensor 'inp' that is not used as input during forward pass:
m = Model()
inp = torch.randn(32, 32)

 # Inputs to the model
 x1 = torch.randn(64, 32)

# Using 'inp' in 'forward' call will add the result of the matrix multiplication operation on tensors 'x1' and 'inp' to 1:
__output__  = m(x1, inp)