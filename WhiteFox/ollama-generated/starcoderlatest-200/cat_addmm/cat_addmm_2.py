
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.addmm(x1, self.mat1, self.mat2) # Perform matrix multiplication
        v2 = torch.cat([v1], dim=0) # Concatenate along the dimension corresponding to the value of 'dim'
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
