
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2048, x256):
        v1 = torch.cat([x2048, x256], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:size]
        v4 = torch.cat([v1, v3], dim=1)
        return v4

# Initializing the model
m = Model()

# Input to the model
x2048  = torch.randn(16, 2048)
x256   = torch.randn(size, 256)
__output__  = m(x2048, x256)

