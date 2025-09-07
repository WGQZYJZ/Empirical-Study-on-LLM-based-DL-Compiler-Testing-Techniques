
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1, x2):
        return torch.mm(x1, x2) + self.dim
 
 # Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
x2 = torch.randn(3, 8, 64, 64)
