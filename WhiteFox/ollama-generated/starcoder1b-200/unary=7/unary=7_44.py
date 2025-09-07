
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(8, 6)
 
    def forward(self, x):
        l1  = self.linear1(x)
        l2  = self.linear2(l1)
        l3  = (l2 + 3) / 6
        return l3


# Initializing the model
m = Model()

