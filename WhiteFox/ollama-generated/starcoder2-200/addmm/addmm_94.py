
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2):
        v1 = torch.mm(inp1, inp2)
        v2 = v1 + inp
        return v2


# Initializing the model and inputs for it
m  = Model()
i1 = torch.randn((4096), (3))
i2 = torch.randn((4096), (3))

