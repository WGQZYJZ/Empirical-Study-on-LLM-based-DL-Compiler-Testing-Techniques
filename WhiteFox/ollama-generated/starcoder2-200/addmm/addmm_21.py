
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1=None, inp2=None):
        t1 = torch.mm(inp1, inp2)
        t2  = t1 + inp 
        return t2


# Initializing the model