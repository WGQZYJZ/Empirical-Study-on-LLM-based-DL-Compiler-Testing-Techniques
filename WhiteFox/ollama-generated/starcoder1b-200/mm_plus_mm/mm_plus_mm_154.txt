
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(3, 4)
        self.m2 = torch.nn.Linear(4, 5)
 
    def forward(self, x1, x2):
        m1 = self.m1(x1)
        m2 = self.m2(x2)
        return m1 + m2


# Initializing the model
m = Model()

