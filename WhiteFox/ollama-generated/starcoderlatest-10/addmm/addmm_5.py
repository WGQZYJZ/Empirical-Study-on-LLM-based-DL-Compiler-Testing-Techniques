
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        return v1 + self.inp


# Inputs to the model
x1 = torch.randn(4, 3)
x2 = torch.randn(4, 3)
m = Model(x2)
