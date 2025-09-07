
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(3, 4)
        self.m2 = torch.nn.Linear(5, 6)
 
    def forward(self, x1, x2):
        y1 = self.m1(x1)
        y2 = self.m2(x2)
        return t3


# Initializing the model
m  = Model()
x1 = torch.randn(4, 3)
x2 = torch.randn(6, 5)
