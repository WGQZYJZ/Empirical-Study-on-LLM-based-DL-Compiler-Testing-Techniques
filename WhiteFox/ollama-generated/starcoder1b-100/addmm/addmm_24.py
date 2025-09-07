
class Model(torch.nn.Module):
    def __init__(self, inp: torch.Tensor=None):
        super().__init__()
        self.inp = inp
 
    def forward(self, x1, x2):
        return torch.mm(x1, x2) + self.inp


# Initializing the model
m = Model()


