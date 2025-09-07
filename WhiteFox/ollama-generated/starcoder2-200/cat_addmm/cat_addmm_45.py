
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
       # input 1
       v2 = torch.addmm(x1, mat1, mat2)
       v3 = torch.cat([v2], dim=0) 
       return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(batch_size, 8*8) # 2D
__output__  = m(x1)

Inputs to the model
x1 = torch.randn(batch_size, 3, 64, 64) # 4D