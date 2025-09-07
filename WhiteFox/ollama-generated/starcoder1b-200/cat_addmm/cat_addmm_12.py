
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(8, 4)
 
    def forward(self, x1, x2):
        t1 = torch.addmm(x1, x2, torch.cat([x1], dim=0))
        t2 = torch.cat([t1], dim=0)
        t3 = self.linear1(t2)
        t4 = self.linear2(t3)
        return t4


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
