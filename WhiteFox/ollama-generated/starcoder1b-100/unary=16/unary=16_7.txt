
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(64*128, 50)
 
    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model()


