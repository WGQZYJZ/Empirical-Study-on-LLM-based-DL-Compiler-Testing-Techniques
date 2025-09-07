
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        t1 = torch.cat([x[:, 0:64], x[:, 9223372036854775807:]], dim=1)
        t2 = t1[:, 0:64] * 0.5
        t3 = t1[:, 9223372036854775807:] * 0.7071067811865476
        return torch.cat([t2, t3], dim=1)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2, 3, 64, 64)
