

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, inp):
        t1 = torch.mm(input1, input2)
        t2 = t1 + inp
        return t2


# Initializing the model
m  = Model()
x1  = torch.randn(30, 45, requires_grad=True) # 3D tensor with shape (30, 45). The 3rd dimension is of size 8.
x2  = torch.randn(39, 67)   # 2D tensor with shape (39, 67).

