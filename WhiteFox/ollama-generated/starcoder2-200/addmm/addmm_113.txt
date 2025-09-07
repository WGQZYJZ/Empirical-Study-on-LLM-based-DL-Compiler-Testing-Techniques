
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm  = torch.matmul
 
    def forward(self, inp1, inp2):
        v1  = self.mm(inp1, inp2)
        return v1 + inp


# Initializing the model
m  = Model()

# Inputs to the model
__output__  = m(x1, x2)

