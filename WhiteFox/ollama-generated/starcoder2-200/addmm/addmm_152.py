
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2):
        v = torch.mm(inp1, inp2) + inp  # perform a matrix multiplication and add it to another tensor 'inp'
        return v


# Initializing the model
m  = Model()
 
# Inputs to the model: input tensors, 'inp': 4-D tensor; 3rd dimension: 5; 1st and 2nd dimensions: 3*6.
inp_t1  = torch.randn(3, 5)
inp_t2  = torch.randn(6, 5)
__output__  = m(inp_t1, inp_t2)

