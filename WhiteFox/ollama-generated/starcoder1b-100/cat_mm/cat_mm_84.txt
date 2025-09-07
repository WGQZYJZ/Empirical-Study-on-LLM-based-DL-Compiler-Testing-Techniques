
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        return torch.cat([x1 * 2, x2 * 3], dim=-1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 64, 64)
x2 = torch.randn(1, 64, 64)
