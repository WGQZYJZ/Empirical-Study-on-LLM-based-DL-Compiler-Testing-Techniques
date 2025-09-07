
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, inp=None):
        v1 = torch.mm(x1, x2)
        if (inp is None):
            v2  = v1 + 5
        else:
            v2  = v1 + inp
        return v2
 
m  = Model()

 # Initializing the model
m(torch.randn(300), torch.randn(400, 6))
