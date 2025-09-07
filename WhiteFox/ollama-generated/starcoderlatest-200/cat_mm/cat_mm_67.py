
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1, x2)  # The number of times the matrix multiplication result is concatenated depends on the length of the list in the `torch.cat` function.
        v2 = torch.cat([v1, v1, ..., v1], dim=0)
        return v2
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
