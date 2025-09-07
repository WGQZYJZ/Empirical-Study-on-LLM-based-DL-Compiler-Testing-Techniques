
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2):
        v1 = torch.mm(inp1, inp2) + inp2
        return v1
 
 
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3)
x2 = torch.randn(1, 4)
