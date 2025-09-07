
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1, torch.randn(256))
        v3 = 0.7 * v1 + inp 
        return v3


# Initializing the model
m = Model()


# Inputs to the model
input1 = torch.rand(48, 256) # Randomly generated tensor of shape (48 x 256) that serves as input for matrix multiplication.
input2 = torch.rand(256, 3072) # Another randomly generated tensor of shape (256 x 3072) that is used in the matrix multiplication operation.
inp = torch.rand(48,) # A third random tensor used as input for matrix multiplication with shape (48,)
