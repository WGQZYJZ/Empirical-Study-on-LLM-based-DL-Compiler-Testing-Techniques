

class Model(torch.nn.Module):
    def __init__(self, dim=10, inSize=32):
        super().__init__()
        self.linear  = torch.nn.Linear(inSize, 4)
        self.layernorm  = torch.nn.LayerNorm(dim, elementwise_affine=True)
 
    def forward(self, x1):
        v1  = torch.addmm(x1, mat2, mat3)
        v2  = torch.cat([v1], dim)
        return v2

m = Model()
x1  = torch.randn(4096*8, inSize=7, device="cuda") # Inputs to the model - 4096 batches of size 3
__output__  = m(x1)

