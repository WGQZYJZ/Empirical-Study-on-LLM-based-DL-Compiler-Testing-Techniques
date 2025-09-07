
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.split(x1, 368, dim=0)
        return torch.cat([v for _, v in enumerate(v2)], dim=0), [len(v2), len(v)]

# Initializing the model
m  = Model()
__output__, s  = m(torch.randn(1548, 3, 6))

# Input to the model
t_input  = torch.rand(1024)

