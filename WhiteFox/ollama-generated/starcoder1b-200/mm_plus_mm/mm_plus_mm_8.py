
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        return torch.mm(x1, x2) + torch.mm(x1, x2)

 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(4, 8, 3, 3)
x2 = torch.randn(4, 8, 3, 3)
