
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, x1)
        if (inp != None):
            v2 = v1 + inp
        return v2


# Initializing the model
m = Model()

