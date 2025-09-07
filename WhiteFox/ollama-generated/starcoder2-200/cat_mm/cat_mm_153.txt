
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2): 
        v = torch.mm(x1, x2) 
        v  = torch.cat([v for i in range(5)], dim=0)
        return v


# Initializing the model
m  = Model()

# Inputs to the model: 3D input tensors, different from the previous one.
x1  = torch.randn(4, 28, 7)
x2  = torch.randn(7, 56, 30)

 __output__   = m(x1, x2)
