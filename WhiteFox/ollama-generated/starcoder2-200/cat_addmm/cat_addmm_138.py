
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.addmm(x1[0], x2[0].transpose(-3, -2), x2[1]) + x1[1] # Apply matrix multiplication to two tensors and then concatenate along the final dimension.
        return v1


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = [torch.randn(4, 3), torch.randn(5, 6)]
x2  = [torch.randn(7, 8), torch.randn(9, 10)]
__output__  = m(x1, x2)

