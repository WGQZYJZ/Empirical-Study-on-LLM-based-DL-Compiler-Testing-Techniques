
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(4, 4)
 
    def forward(self, x1):
        m1 = self.linear1(x1)
        m2 = m1 + 1
        m3 = torch.cat([m2], dim=1)
        m4 = self.linear2(m3)
        return m4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 4, 32, 32)
