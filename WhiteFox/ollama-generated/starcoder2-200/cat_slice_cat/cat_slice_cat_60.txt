
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v0 = [x1]
        v1 = []
        for v in range(len(v0)):
            v1 += [torch.cat([v0[v], v0[v]], dim=1)]
        v2  = torch.stack(v1).squeeze()
        v3 = v2[:, 0:9223372036854775807] 
        v4 = v3[:, 0:size]  
        v5 = []
        for v in range(len(v4)):
            v5 += [torch.cat([v1[v], v4[v]], dim=1)]
        return torch.stack(v5).squeeze()


# Initializing the model
m = Model()


# Inputs to the model