
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = torch.cat([v1[:, 0:9223372036854775807], v1], dim=1)
        v3 = torch.cat([x3, v2], dim=1)
        return v3


# Initializing the model
m = Model()

