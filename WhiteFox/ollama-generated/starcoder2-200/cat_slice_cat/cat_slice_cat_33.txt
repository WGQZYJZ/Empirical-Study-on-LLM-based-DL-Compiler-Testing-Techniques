
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, *args):
        v0 = torch.cat([*args], dim=1)
        return v0[:, 0:9223372036854775807][:size]


# Initializing the model
m  = Model()


# Inputs to the model
x1, x2 = torch.randn(1, 3, 64, 64), torch.randn(1, 9223372036854775807)
__output__  = m(x1, x2)

