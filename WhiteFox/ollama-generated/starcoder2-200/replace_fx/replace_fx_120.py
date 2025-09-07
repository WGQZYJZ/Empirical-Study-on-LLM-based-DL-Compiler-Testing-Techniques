
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.nn.functional.dropout(x1, 0.3)
        v3 = torch.rand_like(v2)
        return v3


# Initializing the model and running it on the CPU device:
m = Model()
m.cpu()
x1 = torch.randn(4)
