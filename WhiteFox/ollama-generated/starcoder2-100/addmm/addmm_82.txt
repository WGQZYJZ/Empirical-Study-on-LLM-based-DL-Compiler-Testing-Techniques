
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, inp1, inp2):
        v1 = torch.mm(inp1, inp2)
        v2 = v1 + inp
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
a1 = torch.randn([32,64])
a2 = torch.randn([64,85])
inp = torch.randn(32)
__output__= m(a1, a2)

