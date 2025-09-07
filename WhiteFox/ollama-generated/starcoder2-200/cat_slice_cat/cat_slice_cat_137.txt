
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.cat([x1[0], x1[-1]], dim=1)
        return v2


# Initializing the model