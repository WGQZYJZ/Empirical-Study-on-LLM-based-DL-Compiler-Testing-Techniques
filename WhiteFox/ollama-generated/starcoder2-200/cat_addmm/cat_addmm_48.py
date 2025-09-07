

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.addmm(x1, mat1, mat2)
        v2  = torch.cat([v1], dim=0) # Concatenate along dimension 1
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model 
x1 = torch.randn(34560, 784)
mat1 = torch.randn(784, 999)
mat2 = torch.randn(999, 34560)

