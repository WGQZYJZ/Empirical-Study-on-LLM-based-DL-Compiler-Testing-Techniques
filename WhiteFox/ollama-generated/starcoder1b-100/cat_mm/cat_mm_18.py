
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 64)
        self.linear2 = torch.nn.Linear(64, 64)
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1, v1, ..., v1])
        return v2


# Initializing the model
m = Model()


