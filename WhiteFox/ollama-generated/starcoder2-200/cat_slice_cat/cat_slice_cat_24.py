
class Model(torch.nn.Module):
    def __init__(self, size=500000):
        super().__init__()
    
    def forward(self, t1, t2): 
        v1 = torch.cat([t1, t2], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:size]
        v4 = torch.cat([v1, v3], dim=1)
        return v4


# Initializing the model
m = Model(2**30+1-9223372036854775807)


