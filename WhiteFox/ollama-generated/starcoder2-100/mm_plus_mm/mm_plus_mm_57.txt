
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, z2):
        v1  = torch.mm(x1, y1) # Matrix multiplication between input1 and input2 
        v2  = torch.mm(z1, z2) # Matrix multiplication between input3 and input4
        v3  = v1 + v2 # Addition of the results of the two matrix multiplications
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(64, 3)  # A 3-D tensor with shape (N, M)
y1 = torch.randn(32, 8)  # A 2-D tensor with shape (N1, M1), where N is larger than N1 and M is larger than M1
z1 = torch.randn(64, 5)  # A 2-D tensor with shape (N2, M2), where N is larger than N2 or M is larger than M2
z2 = torch.randn(8, 7)   # A 3-D tensor with shape (N1, M, M1)

__output__  = m(x1, y1, z1, z2)

