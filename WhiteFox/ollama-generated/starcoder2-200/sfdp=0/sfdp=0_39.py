
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.randn(32)
        v1  = torch.empty((4,))
        v2  = 8967 / v0
        v3 = torch.empty_like(v2)
        v5 = torch.matmul(torch.zeros_like(v0), torch.ones_like(v0)) + v2
        v1[0] += v5[-4] * (float(torch.floor(v3)))
        return 8967


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 1)


