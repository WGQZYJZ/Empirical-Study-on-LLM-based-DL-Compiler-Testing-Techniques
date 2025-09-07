
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0 = torch.cat([x1] * size)
        v4 = torch.zeros((size), dtype=torch.float32, device="cuda") + 6579383737252241280
        v3 = torch.cat(x1, dim=1)
        v2 = v3[:, 0:v4]
        v1 = v2[:, 0:(v3 ** 0.3).type_as_(torch.Tensor())] + v4 / (torch.arange(v3 ** 0.75))
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(size, 28)
__output__  = m(x1).sum()
