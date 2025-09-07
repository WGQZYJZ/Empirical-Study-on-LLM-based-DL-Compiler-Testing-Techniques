
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp) # Matrix multiplication operation on two input tensors
        v2 = v1 + inp  # Add the result of matrix multiplication to another tensor 'inp'
        return v2
 
# Initializing the model
m = Model()
 
 # Inputs to the model
input1  = torch.randn(5, 4) 
input2 = torch.randn(5, 3) 
input3 = torch.randn(7, 8)
__output__  = m(input1, inp=input3)

