
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, inp1, input2=None):
        v1 = torch.mm(inp1, input2)
        v2 = v1 + inp  # Error
        return v2

# Initializing the model