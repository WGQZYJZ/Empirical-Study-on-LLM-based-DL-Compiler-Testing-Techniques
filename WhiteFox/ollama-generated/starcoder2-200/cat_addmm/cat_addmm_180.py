

class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1):
        m1  = torch.randn(50*32*64)
        m2  = torch.randn(50*32*64, 8)
        v1  = torch.addmm(x1, m1, m2)
        return torch.cat([v1], self.dim)


# Initializing the model