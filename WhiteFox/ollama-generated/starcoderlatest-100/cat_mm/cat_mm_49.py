
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1, v1])  # The number of times the matrix multiplication result is concatenated depends on the length of the list in the `torch.cat` function
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 3)
x2 = torch.randn(10, 4)
