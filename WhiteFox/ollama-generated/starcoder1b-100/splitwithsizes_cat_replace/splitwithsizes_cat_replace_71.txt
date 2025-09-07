
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        x1 = torch.split(x1, [8, 8], dim=-1)
        x2 = torch.split(x2, [4, 4], dim=-1)
        result = torch.cat([x1[0], x2[0]], dim=0) + torch.cat([x1[1], x2[1]], dim=0)
        return result


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(2, 3, 64, 64)
x2  = torch.randn(2, 8, 64, 64)
