
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1, x2)
        inp = torch.zeros_like(v1)
        return v1 + inp

 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(3, 4, 64, 64)
