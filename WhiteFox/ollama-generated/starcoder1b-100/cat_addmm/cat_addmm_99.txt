
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(12, 1)
 
    def forward(self, x1):
        v1 = self.fc(x1)
        return v1


# Initializing the model
m = Model()

