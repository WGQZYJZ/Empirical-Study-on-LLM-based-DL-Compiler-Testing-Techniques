
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v  = torch.mm(x1, x2) # Matrix multiplication of two input tensors
        v  = torch.cat([v, v, ..., v])
        return v


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 1, 64, 64)
x2 = torch.randn(3, 1, 64, 64)
