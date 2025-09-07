
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2=None):
        if inp2 is None:
            v = self.matrix_mul(inp1)
        else:
            v = self.matrix_mul(inp1, inp2) + inp
        return v
    
    def matrix_mul(self, x1, x2):
        v = torch.mm(x1, x2)
        return v


# Initializing the model
m = Model()
