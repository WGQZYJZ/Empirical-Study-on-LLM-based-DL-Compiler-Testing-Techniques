
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3, 8)
        self.fc2 = torch.nn.Linear(8, 8)
 
    def forward(self, x1, x2):
        # Fully connected layers
        v1  = self.fc1(x1)
        v2  = torch.cat([v1], dim=-1)
        v3  = self.fc2(v2)
 
        return v3


# Initializing the model
m = Model()

