
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm1 = torch.nn.Linear(64, 50)
        self.mm2 = torch.nn.Linear(300, 784)
 
    def forward(self, x1, x2):
        v1 = self.mm1(x1)
        v2 = self.mm2(v1)
        return torch.mm(v2, v2)


# Inputs to the model
x1 = torch.randn(10, 64)
x2 = torch.randn(10, 300)
