
class Model(torch.nn.Module):
    def __init__(self, dim=30):
        super().__init__()
 
        self.linear1  = torch.nn.Linear(dim, dim)
        self.linear2  = torch.nn.Linear(dim, 8 * 64 ** 2)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v3  = self.linear2(v1)
        v2 = v3.reshape(-1, 8, 64 ,64)
        return torch.cat([v2], dim=0)


# Initializing the model
m  = Model()
__output___ = m(x1)

