
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 5)
        self.linear2 = torch.nn.Linear(3, 6)
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2)
        v2 = torch.cat([v1, v1, ..., v1], dim=0)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 2, 10, 15)
x2 = torch.randn(3, 5, 10, 20)
