
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear(12, 4)
 
    def forward(self, x1, x2):
        v1  = self.mm(x1)
        v2 = v1 + x2  # Add the result of the matrix multiplication to a tensor 'x2'
        return v2


# Inputs to the model
x1 = torch.randn(1, 12, 4)
inp = torch.randn(1, 8, 2)
