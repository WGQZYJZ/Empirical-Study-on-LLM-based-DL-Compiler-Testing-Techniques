
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2) # Matrix multiplication between x1 and x2
        v2 = t1  + t2  # Addition of the results of the two matrix multiplications
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 400, 400)
x2 = torch.randn(8, 8, 1, 1)
__output__  = m(x1, x2)

