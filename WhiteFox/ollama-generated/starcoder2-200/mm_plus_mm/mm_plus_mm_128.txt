
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2)
        return torch.mm(v1, v1), torch.mm(v1, v1), torch.mm(x1, v1 + x2)


# Initializing the model
m  = Model()
__output__  = m(torch.randn(4, 32), torch.randn(4, 32))
