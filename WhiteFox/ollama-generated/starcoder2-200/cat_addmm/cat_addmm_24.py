
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()

    def forward(self, x1):
        v1 = torch.addmm(x1, mat1, mat2)  # Matrix multiplication
        v2 = torch.cat([v1], dim)        # Concatenate along a dimension 
        return v2

# Initializing the model and specifying the concatenation dimension
m  = Model()

 # Inputs to the model
x1  = torch.randn(50, 3, 64, 64)
  __output__  = m(x1)

