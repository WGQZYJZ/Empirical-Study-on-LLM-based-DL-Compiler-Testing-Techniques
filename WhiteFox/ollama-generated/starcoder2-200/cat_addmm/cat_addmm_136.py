
class Model(torch.nn.Module):
    def __init__(self, dim=2):
        super().__init__()
        self.dim = 1  # Specify the dimension to be concatenated

    def forward(self, x1):
        v1 = torch.addmm(x1, mat1, mat2)  # Perform a matrix multiplication of mat1 and mat2 and add it to the input tensor
        return torch.cat([v1], self.dim)


m = Model()

# Inputs to the model
__input__ = torch.randn(432, 7865907, dtype=torch.double) # Specify a random tensor of shape (number_of_features x 7865907)
__output__  = m(__input__)

