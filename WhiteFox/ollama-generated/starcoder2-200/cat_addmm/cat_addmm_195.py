
class Model(torch.nn.Module):
    def __init__(self, dim=10):
        super().__init__()
 
    def forward(self, x1):
        t1  = torch.addmm(x1, torch.randn((3 * 8, 8)), torch.randn((3*8)))
        t2  = torch.cat([t1], dim)
        return t2

# Initializing the model with a dimension of 5
m = Model(dim=5)

