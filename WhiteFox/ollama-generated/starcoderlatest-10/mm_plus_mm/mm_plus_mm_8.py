
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 16)
        self.linear2 = torch.nn.Linear(16, 32)
 
    def forward(self, x1, x2):
        v1 = self.linear1(x1)
        v2 = self.linear2(v1)
        v3 = torch.mm(v2, v1.T)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8)
x2 = torch.randn(1, 32)
