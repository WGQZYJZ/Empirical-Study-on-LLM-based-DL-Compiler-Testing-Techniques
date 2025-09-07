
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, w2, t4):
        v0  = torch.mm(x1,y1) # Matrix multiplication between input1 and input2
        v1  = torch.mm(z1,w2) # Matrix multiplication between input3 and input4
        v2  = v0 + v1         # Addition of the results of the two matrix multiplications
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(6,7)
y1 = torch.randn(4,3)
z1 = torch.randn(5,3)
w2 = torch.randn(4,8)
t4 = torch.randn(8,)
 
__output__  = m(x1, y1, z1, w2, t4)

