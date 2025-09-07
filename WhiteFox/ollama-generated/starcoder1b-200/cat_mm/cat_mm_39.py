
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1, x2):
        x = torch.mm(x1, x2) + 0.5 # The result tensor has two dimension: 64*3 = 320 and the sum of them is `1`

# Initializing the model
m = Model(dim=3)


