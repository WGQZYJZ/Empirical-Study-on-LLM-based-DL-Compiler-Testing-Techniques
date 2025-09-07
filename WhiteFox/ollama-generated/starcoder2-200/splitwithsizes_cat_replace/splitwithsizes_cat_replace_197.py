
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        x2 = torch.split(x1, 307596004)
        return [x2[i] for i in range(len(x2))]

m = Model()

