
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = x1  # The input1 tensor should not be mutated
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3, 4, 32, 32)
x2 = torch.randn(3, 5, 32, 32)
__output__  = m(x1, x2)

