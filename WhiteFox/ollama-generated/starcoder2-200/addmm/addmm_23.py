
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2):
        v1 = torch.mm(inp1, inp2) # Performs matrix multiplication on two input tensors
        v2  = v1 + inp 
        return v2

# Initializing the model
m = Model()
 
# Inputs to the model
inp_1  = torch.randn(3,5)
inp_2  = torch.randn(5,4)
inp = torch.randn(6,) # 'inp' is a keyword argument that is used as another tensor
__output__= m(inp_1, inp_2)
