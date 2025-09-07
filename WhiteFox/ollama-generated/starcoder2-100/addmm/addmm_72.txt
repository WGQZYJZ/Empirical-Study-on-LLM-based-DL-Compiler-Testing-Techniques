
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        return v1 + inp


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(500, 346) # Input tensor for 'inp'
__output__, inp  = m(x1, x2) # Input tensors for 'input1', and 'input2'

