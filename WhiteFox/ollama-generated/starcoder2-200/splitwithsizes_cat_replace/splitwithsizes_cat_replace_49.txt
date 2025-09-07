
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0  = torch.split(x1, 32, dim=0)
        v1  = torch.cat([v for i in range(len(v0))], dim=-1)
        return v1


# Initializing the model
m  = Model()
