
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2):
        v1 = torch.mm(inp1, inp2)
        v2 = v1 + inp  # We add a tensor to the result of matrix multiplication using the keyword argument
        return v2


# Initializing the model
m = Model()
 
x1 = torch.randn(4, 5).to('cpu')
x2 = torch.randn(4, 5).to('cpu')
