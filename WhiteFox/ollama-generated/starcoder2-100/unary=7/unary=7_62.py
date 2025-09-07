
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = torch.nn.Linear(784, 500)
        self.l2 = torch.nn.Linear(500, 300)
        self.l3 = torch.nn.Linear(300, 10)
 
    def forward(self, x):
        l1 = self.l1(x)
        l2 = self.l2(clamp(min=0, max=6, l1 + 3))
        l3 = self.l3(l2 / 6)
        return l3

