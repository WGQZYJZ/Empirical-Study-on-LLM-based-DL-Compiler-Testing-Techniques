
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear(3, 8)
 
    def forward(self, x1, inp):
        v1  = self.mm(x1)
        v2 = v1 + inp
        return v2


# Inputs to the model
m = Model()
x1 = torch.randn(3, 4, requires_grad=True)
inp  = torch.randn(8)
