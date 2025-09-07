
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, x2, x3)
        v2 = torch.cat([v1], dim=1)
        return v2


# Initializing the model
m = Model()


