
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(2048, 365)
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, x2, input=x2)
        v2 = torch.cat([v1], dim=1)
        return self.fc1(v2)


# Initializing the model
m = Model()


