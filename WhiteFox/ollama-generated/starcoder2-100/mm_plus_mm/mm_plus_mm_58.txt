

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, a1):
        v1  = torch.mm(x1, y1) + torch.mm(z1, a1)
        return v1

m = Model()

 # Inputs to the model
x1 = torch.randn(567034, 8)
y1 = torch.randn(295015, 8)
z1 = torch.randn(1010243, 8)
a1 = torch.randn(250222, 8)

 # Initializing the model 
 m(x1, y1, z1, a1)