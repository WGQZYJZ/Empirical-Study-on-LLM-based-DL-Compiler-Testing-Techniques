
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, 3)
        v2 = v1.permute(0, 2, 1).reshape(3, -1, 5)

        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(4, 8)
__output__  = m(x1)
