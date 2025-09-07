
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, inp1=None, inp2=None):
        if inp1 is None:
            inp1 = torch.randn((1, 3))
        if inp2 is None:
            inp2 = torch.randn((1, 4))
        v = torch.mm(inp1, inp2) + inp2
        return v


# Initializing the model
m = Model()
