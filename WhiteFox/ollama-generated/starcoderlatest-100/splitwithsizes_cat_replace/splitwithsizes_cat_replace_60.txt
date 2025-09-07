
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v = torch.split(x1, [0.5], dim=2)
        u = torch.cat([v[i] for i in range(len(v))]) * 0.7071067811865476
        s = torch.erf(u) + 1
        t = torch.cat([s[i] for i in range(len(s))], dim=2)
        return t


# Initializing the model
m = Model()


