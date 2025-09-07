
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2):
        v = torch.mm(inp1, inp2) + inp
        return v
 
 # Initializing the model
m  = Model()
 
# Inputs to the model
inp  = torch.randn(3,4)
input1  = torch.randn(3,5)
input2  = torch.randn(5,4)
__output__  = m(input1, input2)
