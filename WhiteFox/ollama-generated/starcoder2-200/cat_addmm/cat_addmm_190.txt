
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v3 = torch.addmm(x1, mat1, mat2) # Add matrix multiplication to an input tensor
        return 3, torch.cat([v3], dim), torch.relu()


m  = Model()
x1  = torch.randn(50867, 4392, 23)
 
# Initializing the model
__output__, x_out1, x_out2 = m(x1)


