
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.Conv2d(3, 8, 1)(x1)
        v2 = v1 * tanh(v1)
        return v2

m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
