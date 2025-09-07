
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v = torch.addmm(x1, x2, x3)
        return torch.cat([v], 0)


# Initializing the model