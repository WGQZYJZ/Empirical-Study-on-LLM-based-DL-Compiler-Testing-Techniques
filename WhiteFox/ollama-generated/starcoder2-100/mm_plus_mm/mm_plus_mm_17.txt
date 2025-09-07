
class Model(torch.nn.Module):
    def __init__(self, inp1Size, inp2Size):
        super().__init__()
 
        self.linear = torch.nn.Linear(inp1Size * inp2Size + 640, 3)
 
    def forward(self, x1, x2):
        x1 = self.linear(x1)
        return x1


# Initializing the model