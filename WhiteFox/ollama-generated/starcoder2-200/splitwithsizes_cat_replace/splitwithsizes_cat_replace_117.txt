
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.split(x1, 3072 * 4, dim=1) # Split the input tensor into several tensors along a given dimension using `torch.split`
        v4 = torch.cat([v for v in v2], dim=1) # Concatenate the split tensors along the same dimension using `torch.cat`
 
        return v4

m  = Model()
x1 = torch.randn(8, 3075 * 6)
