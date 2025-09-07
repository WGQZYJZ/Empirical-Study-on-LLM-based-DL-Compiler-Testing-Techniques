
class Model(torch.nn.Module):
    def __init__(self, mat1, mat2):
        super().__init__()

    def forward(self, input, dim=0):
        v1  = torch.addmm(input, mat1, mat2) 
        v3  = torch.cat([v1],dim)
        return v3

# Initializing the model
mat_1  = torch.randn(64, 8*8*512), dtype=torch.float)
mat_2  = torch.randn(8*8*512, 4096), dtype=torch.float)
m  = Model(mat_1, mat_2)

# Input to the model: 64x3x8x8
x1  = torch.randn(batch, channels , 8, 8 ) # input tensor of size batch x channel x 8 x 8

