
class Model(torch.nn.Module):
    def __init__(self, inp: torch.Tensor):
        super().__init__()
        self.inp = inp
 
    def forward(self, x1, x2):
        v = torch.mm(x1, x2) + self.inp
        return v


# Inputs to the model
m  = Model()
inp = torch.randn(3, 3)
