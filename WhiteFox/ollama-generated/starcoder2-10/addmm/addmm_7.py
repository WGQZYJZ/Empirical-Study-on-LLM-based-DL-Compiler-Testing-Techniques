
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2):
        v1 = torch.mm(inp1, inp2) + inp  # Add the result of the matrix multiplication to another tensor 'inp'
        return v1


# Initializing the model
m = Model()
inp1  = torch.randn(4096, 512)
inp2  = torch.randn(4096, 512)
__output__  = m(inp1, inp2) # Pass the input tensors as arguments

