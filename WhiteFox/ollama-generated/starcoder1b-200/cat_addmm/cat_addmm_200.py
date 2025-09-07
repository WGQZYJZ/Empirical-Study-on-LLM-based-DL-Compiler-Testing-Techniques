
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3, 8)
        self.fc2 = torch.nn.Linear(8, 4)
 
    def forward(self, x1, x2):
        v1 = self.fc1(x1)
        v2 = v1 * 0.5
        v3 = v2 + 1
        v4 = self.fc2(v3)
        v5 = v2 * v4
        return v5


# Initializing the model
m = Model()

