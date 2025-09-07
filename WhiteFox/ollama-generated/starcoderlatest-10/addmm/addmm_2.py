
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp = None):
        v1 = torch.mm(x1, x2)
        if (inp != None):
            v2 = v1 + inp 
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
