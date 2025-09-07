
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input):
        return torch.nn.functional.batch_norm2d(input, 1) * 3 + 5


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2048, 3, 360, 907)

__output__  = m(x1)