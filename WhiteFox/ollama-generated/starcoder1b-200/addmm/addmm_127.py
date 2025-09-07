
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, inp1, inp2):
        v = torch.mm(inp1, inp2) + inp2
        return v


