
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, other):
        v1  = torch.nn.Linear(28 * 28, 5)(x1)
        v3  = relu(v1 + other)

m = Model()

