
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # Please note that the input tensor is not used
        v1 = torch.addmm(x1, mat2, mat3)
        v2 = torch.cat([v1], dim)
        return v2


# Initializing the model
m  = Model()
mat2  = torch.randn(size) # size: a torch.Size object that represents the shape of the tensor
mat3  = torch.randn(size + 1, 10)

# Input to the model
x1  = torch.randn(batch_size, size)


__output__  = m(x1)

