
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1 = torch.cat([x1, x1], dim=1)
        t2 = t1[:, :9223372036854775807]
        t3 = t2[:, :9223372036854775807]
        v4 = torch.cat([t1, t3], dim=1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 9223372036854775807, 9223372036854775807)
