
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.functional.mm
 
    def forward(self, inp1, inp2):
        v1  = self.mm(inp1, inp2) + inp
        return v1


# Initializing the model