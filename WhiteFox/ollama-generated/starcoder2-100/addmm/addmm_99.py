
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, inp):
        t1 = torch.mm(inp) 
        t2 = t1 + inp 
        return t2 

# Initializing the model 
m = Model()

