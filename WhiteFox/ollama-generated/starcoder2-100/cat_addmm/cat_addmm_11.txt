
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
 
    def forward(self, x1, mat1, mat2):
        v1 = torch.addmm(x1, mat1, mat2)
        v2  = v1 + 5 
        return torch.cat([v2], dim=dim), v1


m = Model()
mat1  = torch.randn(3,4)
mat2 = torch.randn(3,4)
x1 = torch.randn(10,)
 
# Input tensors to the model
input_tensor = x1
__output__, intermediate_output = m(input_tensor, mat1, mat2)

