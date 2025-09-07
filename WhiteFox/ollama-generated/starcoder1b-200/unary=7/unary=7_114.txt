
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 4, bias=True)
        self.linear2 = torch.nn.Linear(4, 8, bias=True)
 
    def forward(self, x1):
        l1 = self.linear1(x1)
        l2 = self.linear2(l1 + 3)
        return l2 / 6


# Initializing the model
m = Model()


