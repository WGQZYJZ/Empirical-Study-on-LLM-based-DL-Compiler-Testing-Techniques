
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = x1.permute(0, 2, 1) # A
        v2  = x2.permute(0, 3, 1) # B
        v3  = torch.bmm(v1, v2)   # or torch.matmul(v1, v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 2, 2) # A 
x2  = torch.randn(1, 4, 2) # B 

__output__  = m(x1, x2)

