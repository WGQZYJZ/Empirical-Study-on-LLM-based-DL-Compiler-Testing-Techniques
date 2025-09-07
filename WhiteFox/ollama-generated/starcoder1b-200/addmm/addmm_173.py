
class Model(torch.nn.Module):
    def __init__(self, inp=10):
        super().__init__()
        self.inp = torch.tensor(inp)
 
    def forward(self, x1, x2):
        return x2 * x1 + self.inp  # Add the result of the matrix multiplication to another tensor 'inp'


# Initializing the model
m = Model()
x1 = torch.randn(3, 4, 64, 64)
