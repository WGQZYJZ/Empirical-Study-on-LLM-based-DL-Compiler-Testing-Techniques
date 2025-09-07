
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1: torch.Tensor, inp: torch.Tensor):
        v1 = self.layer1(x1)
        v2 = v1 + inp
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
inp1 = torch.randn(1, 3, 64, 64)
inp2 = torch.randn(1, 8, 64, 64)
