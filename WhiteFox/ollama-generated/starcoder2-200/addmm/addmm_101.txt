
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, inp): # inp = 'inp' tensor in the pattern
        v0  = torch.mm(x1, x2) + inp 
        return v0

# Initializing the model
m = Model()

