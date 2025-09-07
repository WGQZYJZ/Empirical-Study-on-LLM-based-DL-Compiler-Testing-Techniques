
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, inp1, inp2):
        v1 = torch.mm(inp1, inp2)
        v2 = v1 + inp2
        return v2

 # Inputs to the model
x1 = torch.randn(20, 5, 32, 32)
