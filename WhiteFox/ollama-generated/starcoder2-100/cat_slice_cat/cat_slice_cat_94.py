
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, size):
        v0 = torch.cat([x1, x2], dim=1)
        v1  = v0[:, 0:9223372036854775807]
        v2  = v1[:, 0:size]
        v3 = torch.cat([v0, v2], dim=1)
        return v3
# Initializing the model
m  = Model()


