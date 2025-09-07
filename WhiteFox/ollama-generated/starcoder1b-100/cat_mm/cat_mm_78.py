
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v1 = self.fc(x1)
        return torch.cat([v1, v1, ..., v1])


# Initializing the model
m = Model()


