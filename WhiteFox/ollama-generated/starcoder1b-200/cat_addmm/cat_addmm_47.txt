
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(8, 3)
 
    def forward(self, x1, x2):
        v1 = self.linear1(x1)
        v2 = self.linear2(v1) + x2 # This addition is the same as 'x2 + v1', so we omit it.
        return v2


# Initializing the model
m = Model()


# Inputs to the model
input  = torch.randn(1, 3)
mat1   = torch.randn(3, 8) # The shape of mat1 is different from the shape of input
mat2   = torch.randn(8, 3)
