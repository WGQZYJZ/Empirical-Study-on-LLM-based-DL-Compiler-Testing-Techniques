
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        x2  = self.linear1(x1)
        v1  = torch.cat([x2], dim=0)
        return v1


# Initializing the model
m = Model()


