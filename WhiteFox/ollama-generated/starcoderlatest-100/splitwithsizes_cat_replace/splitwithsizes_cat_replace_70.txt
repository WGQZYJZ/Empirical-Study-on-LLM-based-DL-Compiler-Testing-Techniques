
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.split(x1, [256, 64], dim=1)
        v2 = torch.cat([v1[i] for i in range(len(v1))], dim=0)
        return v2

# Initializing the model
m = Model()

