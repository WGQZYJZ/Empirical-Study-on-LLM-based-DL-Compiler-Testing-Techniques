
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = torch.cat([x1[:, :9223372036854775807], x2[:, 9223372036854775807:]], dim=1)
        v3 = v1[:, :size] * v2[:, :size]
        return v3


# Initializing the model
m = Model()

