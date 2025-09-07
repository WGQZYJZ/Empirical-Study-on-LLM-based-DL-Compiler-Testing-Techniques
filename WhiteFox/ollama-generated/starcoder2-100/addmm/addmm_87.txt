
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, inp1=None, inp2=None):
        out = torch.mm(inp1, inp2) + inp  # Add the result of the matrix multiplication to another tensor 'inp'
        return out


# Initializing the model
m = Model()

# Inputs to the model
inp_tensor1 = torch.randn(3072)
inp_tensor2 = torch.rand(4, 960)
out_tensor = m(inp_tensor1, inp_tensor2) # Add the result of the matrix multiplication to another tensor 'inp'

