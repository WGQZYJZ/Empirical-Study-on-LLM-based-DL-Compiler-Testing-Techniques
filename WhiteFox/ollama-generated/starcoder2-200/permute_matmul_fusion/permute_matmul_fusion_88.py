
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.bmm(x1, x2)  # or torch.matmul(x1, x2) 
        return v


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(5, 6, 4)
x2  = torch.randn(3, 4, 7) # must have compatible shapes for bmm/matmul: 3 x 7 and 4 x 4
__output__= m(x1, x2)
