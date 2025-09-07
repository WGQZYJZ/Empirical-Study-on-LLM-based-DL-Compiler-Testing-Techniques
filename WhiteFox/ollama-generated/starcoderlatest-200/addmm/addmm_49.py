
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp=None):
        v1 = torch.mm(inp['A'], inp['B'])
        v2 = v1 + inp['inp']
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = {'A': torch.randn(3, 4),
      'B': torch.randn(4, 5),
      'inp': torch.randn(3, 5)}
