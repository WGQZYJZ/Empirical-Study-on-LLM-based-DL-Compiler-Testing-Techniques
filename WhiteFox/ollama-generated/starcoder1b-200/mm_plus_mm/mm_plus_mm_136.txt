
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(3, 4)
        self.m2 = torch.nn.Linear(3, 4)
 
    def forward(self, x1, x2):
        m1 = self.m1(x1)
        m2 = self.m2(x2)
        return m1 * m2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 4, 4)
x2 = torch.randn(1, 4, 4, 4)
