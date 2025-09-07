
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, dim=0):
        v1 = torch.addmm(x1, m1, m2)  # perform a matrix multiplication of mat1 and mat2 and add it to the input
        v2 = torch.cat([v1], dim)  # concatenate along dimension
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 64*64*3, device='cuda')
x2 = torch.randn(1, 8*64*64, device='cuda')
