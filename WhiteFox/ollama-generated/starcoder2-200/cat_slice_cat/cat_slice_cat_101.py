
class Model(torch.nn.Module):
    def __init__(self, size=9223372036854775807):
        super().__init__()
    
    def forward(self, x1s):
            v1 = torch.cat(x1s, dim=1)
            v2 = v1[:, 0:size]
            v3 = v2[:, 0:size]
            v4 = torch.cat([v1, v3], dim=1)
            return v4

# Initializing the model