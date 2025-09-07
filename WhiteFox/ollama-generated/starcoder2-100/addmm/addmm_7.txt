
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm  = torch.mm
 
    def forward(self, inp1, inp2):
        v1  = self.mm(inp1, inp2)
        return v1 + inp


# Initializing the model
m  = Model()
 
 # Inputs to the model
a  = torch.randn(3, 4)
b  = torch.randn(4, 5)
  __output__   = m(a, b)

