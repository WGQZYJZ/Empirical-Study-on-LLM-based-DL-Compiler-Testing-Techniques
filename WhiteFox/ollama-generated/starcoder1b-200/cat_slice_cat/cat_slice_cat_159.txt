
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.cat([x1[:, 0:9223372036854775807], x2[:, 0:9223372036854775807]], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v1[:, 0:9223372036854775807]
        return torch.cat([v2, v3], dim=1)


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 256, 9223372036854775807)
