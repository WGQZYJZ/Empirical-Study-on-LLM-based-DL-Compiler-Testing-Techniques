
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1):
        v1 = torch.mm(x1, y1)  # Matrix multiplication between input and input2
        v3 = torch.mm(z1, y1)  # Matrix multiplication between input4 and input2
        return v1 + v3


# Initializing the model
m = Model()


# Inputs to the model
a  = torch.randn(3, 8)
b  = torch.randn(8, 50)
c  = torch.randn(7, 9)
d  = torch.randn(123, 674)
__output__  = m(a, b, c + d)

