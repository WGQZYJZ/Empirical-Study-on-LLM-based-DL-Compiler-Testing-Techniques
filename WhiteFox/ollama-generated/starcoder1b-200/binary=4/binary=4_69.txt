
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(8, 6)
 
    def forward(self, x1, other):
        v1 = self.linear1(x1)
        v2 = torch.cat((v1, other), dim=0)
        return self.linear2(v2)


# Initializing the model
m = Model()
