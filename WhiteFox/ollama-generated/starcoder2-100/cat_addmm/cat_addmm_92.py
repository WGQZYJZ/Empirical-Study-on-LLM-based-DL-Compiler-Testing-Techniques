
class Model(torch.nn.Module):
    def __init__(self, dim=256):
        super().__init__()
 
    def forward(self, x1, mat1, mat2):
        v1 = torch.addmm(x1, mat1, mat2)
        v2 = torch.cat([v1], dim=dim) # Concatenation along the specified dimension 
        return v2

m  = Model()
mat1  = torch.randn(89573,400)
mat2 = torch.randn(400,65536)
 
# Input to the model
input_tensor = torch.randn(32, 3, 256, 256)
