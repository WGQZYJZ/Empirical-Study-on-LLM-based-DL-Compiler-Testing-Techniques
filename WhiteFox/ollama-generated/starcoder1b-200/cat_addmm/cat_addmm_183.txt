
class Model(torch.nn.Module):
    def __init__(self, dim=2):
        super().__init__()
        self.dim = dim

    def forward(self, x1, x2):
        t1 = torch.addmm(x1, x1, x2)
        t2 = [torch.cat([t1], dim=0)]
        return torch.cat(t2, dim=self.dim)


# Initializing the model
m = Model()

