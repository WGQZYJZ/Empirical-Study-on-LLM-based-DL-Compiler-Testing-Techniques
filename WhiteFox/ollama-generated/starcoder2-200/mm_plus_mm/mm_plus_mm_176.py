
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.mm(x1, x2) # Matrix multiplication between input1 and input2
        v2  = torch.mm(x3, x4) # Matrix multiplication between input3 and input4
        v3  = v1 + v2 # Addition of the results of the two matrix multiplications
        return v3


# Initializing model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 60)
__output__  = m(x1)