
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(32000, 10)
 
    def forward(self, x1):
        v1 = F.relu(self.fc(x1))
        return v1


# Initializing the model
m = Model()

