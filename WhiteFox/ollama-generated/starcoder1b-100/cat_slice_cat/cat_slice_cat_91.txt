
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0, x1):
        return torch.cat([x0[:, 0:9223372036854775807], x1], dim=1)


# Initializing the model
m = Model()
__input__ = torch.randn(1, 1, 64, 64)
x0, x1 = __input__[0:2]
