
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, other):
        v1 = torch.nn.Linear(x1.size(-3), 8)(x1) + other
        return torch.nn.ReLU()(v1)


# Initializing the model
m = Model()
__output_1__ = m(torch.randn(2, 4, 5)) # Outputs: 6 x 4 x 5
__output_2__ = m(torch.randn(3, 4), torch.randn(3, 8)) # Outputs: 9 x 8

