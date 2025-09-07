
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, inp=None):
        v1 = torch.mm(input1, inp)
        return v1 + 0

