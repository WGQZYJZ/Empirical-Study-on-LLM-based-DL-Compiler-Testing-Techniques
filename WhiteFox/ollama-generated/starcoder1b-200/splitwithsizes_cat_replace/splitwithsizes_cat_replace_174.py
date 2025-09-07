
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v = torch.split(x1, 32, 0)
        return torch.cat([v[i] for i in range(3)], dim=0)


# Initializing the model
m = Model()

