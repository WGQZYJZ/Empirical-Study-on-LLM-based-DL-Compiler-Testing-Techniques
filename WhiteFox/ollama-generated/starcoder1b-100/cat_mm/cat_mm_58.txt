
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1, x2):
        return torch.cat([x1, x2, x1], 1)

 # Input to the model
x1 = torch.randn(3, 4, 3)
x2 = torch.randn(4, 5, 3)
