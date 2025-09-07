
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v2 = torch.mm(x1, x1)  # Matmul
        v3 = v2 + inp  # Add the result of matmul to another tensor 'inp'

        return v3

# Initializing the model with input tensors. In this example we pass one additional tensor as an input argument named 'inp'.

m  = Model()
inp1 = torch.randn(8, 4)
inp2 = torch.randn(4, 6)
x1   = [torch.randn(3, 5), torch.randn(7, 9)]

