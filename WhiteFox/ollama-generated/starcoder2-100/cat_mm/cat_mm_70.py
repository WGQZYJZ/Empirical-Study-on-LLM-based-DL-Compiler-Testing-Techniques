
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v  = torch.mm(x1, x2)
        return torch.cat([v] * len([0 for i in range(3)] * 5), dim=2)


# Initializing the model