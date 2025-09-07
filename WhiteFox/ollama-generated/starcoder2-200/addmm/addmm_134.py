
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, inp1=None, inp2=None):
        v1 = torch.mm(inp1, inp2) # Perform matrix multiplication on two input tensors 'inp'
        v2 = v1 + inp  # Add the result of the matrix multiplication to another tensor 'inp'
        return v2


m = Model()
__output__  = m(inp1=torch.randn((40, 30)), inp2=torch.randn((30, 70)))

