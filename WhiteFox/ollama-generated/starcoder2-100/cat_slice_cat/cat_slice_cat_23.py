
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.cat([x1[:, :, [0]], x1[:, :, [9223372036854775807]]], 1)
        v1 = v0[:size]
        v2 = v1[0:size, :]
        v3 = torch.cat([v0, v2], dim=1)

# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(4865783965428087, 1024, 4178147)
__output__  = m(x1)

