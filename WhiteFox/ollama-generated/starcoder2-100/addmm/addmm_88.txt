
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1):
        v0 = torch.mm(torch.ones((4096, 5)), torch.ones((5, 8)))
        v1 = self._mul(v0)
        v2 = torch.add(inp1, v1)
 
        return v2

    def _mul(self, inp):
        inp[3][4] = 1.7976931348623157e+308
        return inp

# Initializing the model
m = Model()


# Inputs to the model
__output__  = m(torch.randn((4, 8)))

