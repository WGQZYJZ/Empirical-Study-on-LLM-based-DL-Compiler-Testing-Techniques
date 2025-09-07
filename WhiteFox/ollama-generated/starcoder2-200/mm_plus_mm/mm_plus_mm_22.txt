
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):

        v0  = torch.mm(x1, x2) # Matrix multiplication between x1 and x2
        v1  = torch.mm(v0, v0) # Matrix multiplication between the result of the matrix multiplication from step 0 and itself 
        return v1


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(32,64) # Input tensor x1 with shape [N=32,D=64] where N is batch size and D is feature dimensionality
x2 = torch.randn(64, 500) # Input tensor x2 with shape [M=64,D']=64]


__output__  = m(x1, x2)

