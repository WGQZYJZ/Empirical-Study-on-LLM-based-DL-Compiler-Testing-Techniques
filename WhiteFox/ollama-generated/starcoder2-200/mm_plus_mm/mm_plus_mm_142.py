
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3  = torch.mm(x1['a'], x1['b']) + torch.mm(x2['c'], x2['d']) # Adding matrix multiplication results of two separate matrix multiplications
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1  = {'a': torch.randn(4, 5), 'b': torch.randn(5, 6)}
x2  = {'c': torch.randn(7, 8), 'd': torch.randn(8, 9)}


