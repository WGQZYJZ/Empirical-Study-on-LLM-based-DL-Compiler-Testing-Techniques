
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, size=320794):
        v1 = torch.cat([x1] * 8 + [None for i in range(size)], dim=1)
        v2 = v1[:, :size]
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 4, 560795)
__output__  = m(x1, size=384449)


