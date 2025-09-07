
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm1 = torch.nn.Linear(5, 20)
        self.mm2 = torch.nn.Linear(5, 30)
 
    def forward(self, x1):
        v1 = self.mm1(x1)
        v2 = self.mm2(x1)
        v3 = v1 + v2
        return v3


# Inputs to the model
x1 = torch.randn(1, 5, 64, 64)
