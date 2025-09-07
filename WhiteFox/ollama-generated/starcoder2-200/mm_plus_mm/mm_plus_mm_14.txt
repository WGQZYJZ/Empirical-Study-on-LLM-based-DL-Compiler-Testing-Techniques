
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.ops._prims.matmul

    def forward(self, x1):
        v1  = self.mm(x1)
        v2  = self.mm(input3) 
        v3  = v1 + v2 # Addition of the results of the two matrix multiplications
        return v3

# Initializing the model
m  = Model()


# Inputs to the model
input3, input4  = torch.randn(size=(576, 8))
x1              = torch.randn(290)
__output__      = m(x1)

