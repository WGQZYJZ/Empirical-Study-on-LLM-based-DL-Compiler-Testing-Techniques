
class Model(torch.nn.Module):
    def __init__(self, inp=torch.tensor([2])):
        super().__init__()
        self.inp = inp
 
    def forward(self, x1, x2):
        return torch.mm(x1, x2) + self.inp


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
inp = torch.tensor([0.5])
