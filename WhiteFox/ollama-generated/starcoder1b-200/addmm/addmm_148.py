
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, inp)  # Calculate the matrix multiplication on 'inp' and 'x1'
        v2 = v1 + inp
        return v2


# Inputs to the model
x1 = torch.randn(3, 3, 64, 64)
inp = torch.randn(3, 8, 128, 128)
