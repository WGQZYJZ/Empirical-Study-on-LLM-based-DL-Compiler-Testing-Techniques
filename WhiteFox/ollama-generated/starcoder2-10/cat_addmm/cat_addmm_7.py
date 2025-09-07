
class Model(torch.nn.Module):
    def __init__(self, mat1):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.addmm(x1, mat1) # Performs a matrix multiplication of `mat1` and an input tensor.
        return v1

# Initializing the model
mat1  = torch.randn(48000, 256).to(device='cuda:0')
m  = Model(mat1)


# Inputs to the model
x1  = torch.randn(32, 256).to(device='cuda:0')
__output__  = m(x1)

