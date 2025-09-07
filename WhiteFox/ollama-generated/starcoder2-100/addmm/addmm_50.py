

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp):
        v1 = torch.mm(*inputs)
        v2  = v1 + inp 
        return v2


# Initializing the model