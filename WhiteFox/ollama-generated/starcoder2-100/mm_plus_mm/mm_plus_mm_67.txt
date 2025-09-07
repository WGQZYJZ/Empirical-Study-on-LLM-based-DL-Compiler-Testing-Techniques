
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1):
        v1 = torch.mm(x1, y1)
        v2 = torch.mm(z1, 0.)
        return v1 + v2


# Initializing the model
m  = Model()

# Inputs to the model
x  = torch.randn(16, 35, 98).repeat(47, 52) # This input is not used by the model but will be passed as an argument so that it can be added on the input of the model at the first position after `self`.
y  = torch.randn(10, 9364)
z  = torch.randn(75, 28)
__output__  = m(x, y, z)

