
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(1024, 5)
 
    def forward(self, x):
        v1 = self.fc(x)
        v2 = torch.relu(v1)
        return v2

# Initializing the model