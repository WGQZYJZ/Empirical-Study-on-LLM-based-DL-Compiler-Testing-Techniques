
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
        self.inp = inp

    def forward(self, x1, x2=None):
        # Do something...
        return out


