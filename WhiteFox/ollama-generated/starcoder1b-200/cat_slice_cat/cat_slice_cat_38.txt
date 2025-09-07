
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4, x5, x6):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = torch.cat([v1[:, 0:9223372036854775807], x3], dim=1)
        v3 = torch.cat([t1[:, 0:size], v2], dim=1)
        v4 = torch.cat([x1, v3], dim=1)
        v5 = torch.cat([v4[:, 0:9223372036854775807], t3], dim=1)
        v6 = torch.cat([t1[:, 0:size], v5], dim=1)
        return v6


# Initializing the model
m = Model()
