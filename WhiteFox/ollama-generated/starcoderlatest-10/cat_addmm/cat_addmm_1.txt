
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.addmm(x1, x2, x1) # Perform a matrix multiplication of x1 and x2 and add it to the input
        t2 = torch.cat([t1], dim) # Concatenate the result along a specified dimension
        return t2


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
x2 = torch.randn(2, 3, 64, 64)
