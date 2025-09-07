
class Model(torch.nn.Module):
    def __init__(self, m1, m2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
        self.mlp = [m1(), m2()]
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = []
        for m in self.mlp:
            v2.append(m(v1))
        return torch.cat(v2, dim=0)


# Initializing the model
m1 = Model(torch.nn.Linear(32 * 64, 8), torch.nn.ReLU())
m2 = Model(torch.nn.Linear(8, 1), torch.nn.Sigmoid())
