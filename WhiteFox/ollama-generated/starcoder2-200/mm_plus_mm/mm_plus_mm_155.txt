

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v0 = torch.mm(x1, x2)
        v1 = torch.mm(x3, x4)
        v2  = v0 + v1 
        return v2


# Initializing the model
m  = Model()
__output__  = m(torch.randn(5), torch.randn(5), torch.randn(7), torch.randn(7))

