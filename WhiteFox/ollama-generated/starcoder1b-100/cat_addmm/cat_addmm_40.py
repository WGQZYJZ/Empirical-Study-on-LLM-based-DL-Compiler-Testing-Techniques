
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3, 8)
        self.fc2 = torch.nn.Linear(8, 6)
 
    def forward(self, x1, x2):
        v1 = self.fc1(x1)
        v2 = self.fc2(v1)
        return v2 + x2


# Initializing the model
m = Model()


