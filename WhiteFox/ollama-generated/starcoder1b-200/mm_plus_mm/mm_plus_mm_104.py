
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v  = torch.mm(x1, x2) + 3
        return v
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 4, 3, 3)
x2 = torch.randn(1, 5, 6, 6)
