
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, size=256):
        v1 = torch.cat([x1[0], x1[1]])
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:size]
        v4 = torch.cat([v1, v3], dim=1)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1  = [torch.randn(56798, 2), 
        torch.randn(70000, 2)]
__output__  = m(x1)
