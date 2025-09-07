
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = torch.nn.Linear(24, 7)
        self.lin2 = torch.nn.Linear(36095, 8)
 
    def forward(self, x1):
        v1 = self.lin1(x1)
        v2 = v1 + self.__other__
        return v2
