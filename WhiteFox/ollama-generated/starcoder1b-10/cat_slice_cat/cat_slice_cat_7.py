
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, y3, y4):
        v1 = torch.cat([x1, y3], dim=1)
        v2 = torch.cat([y2, v1], dim=1)
        v3 = torch.cat([y3, t1], dim=1)
        return v4

# Initializing the model
m = Model()


