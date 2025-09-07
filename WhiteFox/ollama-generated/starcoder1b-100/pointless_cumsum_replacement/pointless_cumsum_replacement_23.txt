
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.full([1, 2], 0.7071067811865476, dtype=torch.double, layout=torch.strided)


# Initializing the model
m = Model()


