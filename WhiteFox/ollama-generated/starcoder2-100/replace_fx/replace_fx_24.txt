
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         # torch.nn.functional.dropout is invoked on the input tensor here.
        v1  = torch.nn.functional.dropout(x1, ...)  
        v2  = torch.rand_like(v1) 
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(3) # 3D tensor here. The first and last dimensions should be the same size.
__output__  = m(x1)

